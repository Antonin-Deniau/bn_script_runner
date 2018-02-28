from binaryninja.plugin import BackgroundTaskThread
import socket, select, sys, traceback, os
import config


def exec_cmd(bv, path):
	source = open(path).read()
	code = compile(source, path, 'exec')
	exec(code, locals())

def start_server(bv):
	sok = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sok.bind((config.host, config.port))

	sok.listen(5)

	while True:
		client, address = sok.accept()

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

		dir_path = os.path.dirname(res)
		sys.path.append(dir_path)

		try:
			exec_cmd(bv, res)
		except:
			traceback.print_exc()
		finally:
			sys.stderr = bak_err
			sys.stdout = bak_out
			sys.path.pop()

			client.shutdown(2)
			client.close()

class Server(BackgroundTaskThread):
	bv = None

	def run(self):
		start_server(self.bv)
