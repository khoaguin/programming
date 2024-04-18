#!/usr/bin/env python3

# tag::TCP_MOJIFINDER_TOP[]
import asyncio
import functools
import sys
from asyncio.trsock import TransportSocket
from typing import cast

from charindex import InvertedIndex, format_results  # <1>

CRLF = b'\r\n'
PROMPT = b'?> '

async def finder(index: InvertedIndex,          # <2>
                 reader: asyncio.StreamReader,
                 writer: asyncio.StreamWriter) -> None:
    client = writer.get_extra_info('peername')  # <3>
    while True:  # <4>
        writer.write(PROMPT)  # can't await!  # <5>
        await writer.drain()  # must await!  # <6>
        data = await reader.readline()  # <7>
        if not data:  # <8>
            break
        try:
            query = data.decode().strip()  # <9>
        except UnicodeDecodeError:  # <10>
            query = '\x00'
        print(f' From {client}: {query!r}')  # <11>
        if query:
            if ord(query[:1]) < 32:  # <12>
                break
            results = await search(query, index, writer)  # <13>
            print(f'   To {client}: {results} results.')  # <14>

    writer.close()  # <15>
    await writer.wait_closed()  # <16>
    print(f'Close {client}.')  # <17>
# end::TCP_MOJIFINDER_TOP[]

# tag::TCP_MOJIFINDER_SEARCH[]
async def search(query: str,  # <1>
                 index: InvertedIndex,
                 writer: asyncio.StreamWriter) -> int:
    chars = index.search(query)  # <2>
    lines = (line.encode() + CRLF for line  # <3>
                in format_results(chars))
    writer.writelines(lines)  # <4>
    await writer.drain()      # <5>
    status_line = f'{"─" * 66} {len(chars)} found'  # <6>
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
