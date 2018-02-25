#!/usr/bin/env python
import socket, sys, select

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('127.0.0.1', 5335))

sended = False

while True:
	try:
		ready_to_read, ready_to_write, in_error = select.select([conn,], [conn,], [])
	except select.error:
		conn.shutdown(2)	# 0 = done receiving, 1 = done sending, 2 = both
		conn.close()
		break

	if len(ready_to_read) > 0:
		recv = conn.recv(2048)
		if not recv: break
		sys.stdout.write(recv)

	if len(ready_to_write) > 0:
		if sended == False:
			message = open(sys.argv[1], "r").read()
			conn.send(message)
			conn.shutdown(1)
			sended = True