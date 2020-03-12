import socket
import rsa_sys
import call_backs

HOST = ''
PORT = 23120
TERM_SIGNAL = '0XDEAD'

class client:
	def __init__(self,socket,addr,id):
		self.client = socket
		self.address = addr
		self.id = id


clients = {}
sock_analitic = {}

def network_thread_proc(socket):
	while True:
		conn, addr = s.accept()
		print('Client => ' + str(addr) + ' Connected')
		try:
			id = conn.recv(2048)
			if id:
				if(rsa_sys.apply_sec(conn,id)):
					clients[id] = client(conn,addr,id)
					call_backs.onconnect(conn, id)
					print('Client => ' + str(addr) + ' Approved')
					if 'sock' in id:
						sock_analitic[id] = client(conn,addr,id)
				else:
					print('Client => ' + str(addr) + ' Rejected')
					continue	
			else:
				print('Client => ' + str(addr) + ' Rejected')
				continue
		except:
		if rsa_sys.apply_sec(conn)

def system_thread_proc():
	for x in clients.values():
		try:
			data = x.recv(2048)
			if data:
				if data != 	TERM_SIGNAL:
					call_backs.onread(x,data,sock_analitic)
				else:
					call_backs.ondisconnect(x)
					del clients[x.id]
					if x.id in sock_analitic.keys():
						del sock_analitic[x.id]					
		except:
			call_backs.onerror(x)


client_no = 1
#buffer_size = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
print('TCP Server Start at %s:%s'%(HOST,PORT))
s.listen(client_no)
#conn, addr = s.accept()
network_thread = threading.Thread(target = network_thread_proc)
network_thread.start()
system_thread_proc()


