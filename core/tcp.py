#in version 3.1+
import socket
class TestServer:
	
	def __init__(self, ip='0.0.0.0', iPort=514):	
		self.ip = ip
		self.iPort = iPort
	
	def start(self):		
		print("TestServer start({0}:{1})...".format(self.ip, self.iPort))
				
		cc = 1		
		ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		ss.settimeout(1000 * 10)
		ss.bind((self.ip, self.iPort))
		ss.listen(5)
		
		while cc <= 5:
			(client, address) = ss.accept()
			print("client connecting:",cc)
			cc+=1
			
			client.send(b'hello')
			client.close()
		ss.close()
		print("TestServer close, bye-bye.")	
	
	
if __name__ == "__main__":
	ts = TestServer()
	ts.start()
