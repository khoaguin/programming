#!/usr/bin/env python3

# tag::TCP_MOJIFINDER_TOP[]
import asyncio
import functools
import sys
from asyncio.trsock import TransportSocket
from typing import cast

from charindex import InvertedIndex, format_results

CRLF = b'\r\n'
PROMPT = b'?> '

async def finder(
    index: InvertedIndex,          # will be wrapped with `functools.partial`
    reader: asyncio.StreamReader,
    writer: asyncio.StreamWriter
) -> None:
    client = writer.get_extra_info('peername')  # get the remote client addr to which the socket is connected
    while True:  # handles a dialog that lasts until a control character is received from the client.
        writer.write(PROMPT)  # can't await!  # normal function that sends the PROMPT
        await writer.drain()  # must await!  # `drain` is a coroutine that flushes the writer buffer
        data = await reader.readline()  # a coroutine that returns bytes
        if not data:  # no bytes received: close the connection
            break
        try:
            query = data.decode().strip()  # Decode the bytes to str using UTF-8 encoding
        except UnicodeDecodeError:  # happen when the client sends `Ctrl-C` (control byte)
            query = '\x00'  # replace the query with a null character
        print(f' From {client}: {query!r}')  # Log the query to the server console.
        if query:
            if ord(query[:1]) < 32:  # Exit the loop if a control or null character was received
                break
            results = await search(query, index, writer)  # Do the actual search; code is presented next
            print(f'   To {client}: {results} results.')  # Log the response to the server console

    writer.close()  # Close the StreamWriter
    await writer.wait_closed()  # Wait for the StreamWriter to close
    print(f'Close {client}.')  # Log the end of this client’s session to the server console.
# end::TCP_MOJIFINDER_TOP[]

# tag::TCP_MOJIFINDER_SEARCH[]
async def search(
    query: str,
    index: InvertedIndex,
    writer: asyncio.StreamWriter
) -> int:
    """
    Does the search functionality. Must be a coroutine since it writes 
    to a `StreamWriter` and must uses the `StreamWriter.drain()` method
    """
    chars = index.search(query)  # query the inverted index
    lines = (line.encode() + CRLF for line  # yield byte strings encoded in UTF-8
                in format_results(chars))
    writer.writelines(lines)  # send the lines
    await writer.drain()      # await for the `StreamWriter.drain()` method
    
    status_line = f'{"─" * 66} {len(chars)} found'  # Build a status line, then send it.
    writer.write(status_line.encode() + CRLF)
    await writer.drain()
    return len(chars)
# end::TCP_MOJIFINDER_SEARCH[]

# tag::TCP_MOJIFINDER_MAIN[]
async def supervisor(index: InvertedIndex, host: str, port: int) -> None:
    server = await asyncio.start_server(    # gets an instance of asyncio.Server (a TCP socket server)
        functools.partial(finder, index),   # a callback to run when a new client connection starts
                                    # use `functools.partial` to bind the `index` parameter
                                    # and obtain a callable that takes asyncio.StreamReader 
                                    # and asyncio.StreamWriter as inputs.
        host, port  # host and port are the second and third arguments to `asyncio.start_server`
    )
    # The below cast is needed because typeshed has an outdated type 
    # hint for the sockets property of the Server class
    socket_list = cast(tuple[TransportSocket, ...], server.sockets)
    addr = socket_list[0].getsockname()
    print(f'Serving on {addr}. Hit CTRL-C to stop.')  # Display the address and port of
                                                    # the first socket of the server.
    await server.serve_forever()  # await on the `server_forever` method so that 
                                # `supervisor` is suspended here. Otherwise it will return
                                # immediately, exiting the program
    # After `main` builds the index and starts the event loop, `supervisor` quickly displays the
    # "Serving on…" message and is suspended at the `await server.serve_forever()` line.
    # At that point, control flows into the event loop and stays there, occasionally coming
    # back to the `finder` coroutine, which yields control back to the event loop whenever it
    # needs to wait for the network to send or receive data.
    # While the event loop is alive, a new instance of the `finder` coroutine will be started
    # for each client that connects to the server. In this way, many clients can be handled
    # concurrently by this simple server. This continues until a `KeyboardInterrupt` occurs
    # on the server or its process is killed by the OS.

def main(host: str = '127.0.0.1', port_arg: str = '2323'):
    port = int(port_arg)
    print('Building index.')
    index = InvertedIndex()  # Build the inverted index
    try:
        asyncio.run(supervisor(index, host, port))  # Start the event loop running supervisor.
    except KeyboardInterrupt:                       # Catch the `KeyboardInterrupt` to avoid a distracting 
                                                    # when stop the server with Ctrl-C
        print('\nServer shut down.')

if __name__ == '__main__':
    main(*sys.argv[1:])
# end::TCP_MOJIFINDER_MAIN[]
