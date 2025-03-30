#!/usr/bin/env python3

import sys

void read_input(char *destination, const char *filename)
{
	read_input_with_limit(destination, filename, 0xffffffffffffffff);
}