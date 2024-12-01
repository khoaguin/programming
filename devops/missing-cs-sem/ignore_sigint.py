#!/usr/bin/env python

# Here’s a minimal example of a Python program that captures SIGINT 
# and ignores it, no longer stopping. To kill this program we can 
# now use the SIGQUIT signal instead, by typing Ctrl-\.

import signal, time

def handler(signum, time):
    print("\nI got a SIGINT, but I am not stopping")

signal.signal(signal.SIGINT, handler)
i = 0
while True:
    time.sleep(.1)
    print("\r{}".format(i), end="")
    i += 1

