#!/usr/bin/env python3
import asyncio
import sys
from keyword import kwlist

from domainlib import multi_probe


async def main(tld: str) -> None:
    tld = tld.strip('.')
    names = (kw for kw in kwlist if len(kw) <= 4)  # Generate keywords with length up to 4.
    domains = (f'{name}.{tld}'.lower() for name in names)  # Generate domain names with the given suffix
    print('FOUND\t\tNOT FOUND')  # Format a header for the tabular output
    print('=====\t\t=========')
    async for domain, found in multi_probe(domains):  # Asynchronously iterate over multi_probe(domains)
        indent = '' if found else '\t\t'  # Set indent to zero or two tabs to put the result in the proper column.
        print(f'{indent}{domain}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        asyncio.run(main(sys.argv[1]))  # Run the main coroutine with the given command-line argument
    else:
        print('Please provide a TLD.', f'Example: {sys.argv[0]} COM.BR')
