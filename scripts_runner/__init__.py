from binaryninja import *
from server import Server

srv = Server("stopped", can_cancel=True)

def server_status(bv, fobj):
	print "[script_server] Server status: %s" % srv.progress

def start_server(bv, fobj):
	if srv.progress == "running":
		print "[script_server] Server already started."
		return
	
	print "[script_server] Starting the server."
	srv.bv = bv
	srv.start()
	srv.progress = "running"
	print "[script_server] Server started."

PluginCommand.register_for_function("[script_server] Server status", "Get the server status", server_status)
PluginCommand.register_for_function("[script_server] Start server", "Start/Restart the server", start_server)
