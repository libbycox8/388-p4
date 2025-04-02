#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'A')
# cannot find the .binsh addr from shellcode
# need padding, something to overwrite the return address, then the ./binsh address (as the argument)