from binaryninja.plugin import BackgroundTaskThread
import socket, select, sys, traceback
import config

def exec_cmd(bv, res):
	cc = compile(res, "<string>", "exec")
 	eval(cc, globals(), locals())

def start_server(bv):
	sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sok.bind((config.host, config.port))

	sok.listen(5)

	while True:
		client, address = sok.accept()
		print "{} connected".format( address )

		res = ""
		while True:
			response = client.recv(1024)

			if response == "":
				break
			else:
				res += response

		bak_out = sys.stdout
		bak_err = sys.stderr

		file = client.makefile('w', 0)

		sys.stdout = file
		sys.stderr = file

		try:
			exec_cmd(bv, res)
		except:
			traceback.print_exc()
		finally:
			sys.stderr = bak_err
			sys.stdout = bak_out

			client.shutdown(2)
			client.close()

class Server(BackgroundTaskThread):
	bv = None

	def run(self):
		start_server(self.bv)
