#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode)

# need to write into a tmp register and then access 
# tmp: rbx, rdx, rcx, rdi, rsi