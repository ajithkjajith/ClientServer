import socket
import signal

s= socket.socket()
def SigHandler(a,vb):
	print("Exiting..")
	exit(0)	

signal.signal(signal.SIGINT,SigHandler)

server_ip="localhost"
s.connect((server_ip,8036))

while(1):

	try:

		data1 = s.recv(1024)
		print(data1)

		s.send(bytes("I'm ready to send information"))

		s.recv(1024) #Send contents to save in a file

		s.send(bytes("write")) #for saving contents in server as a file
		s.send(bytes("Hey, this is client information. "))

		yes = s.recv(1024) #we recieved your info and uploaded to the file
		print(yes)

		s.send(bytes("append"))
		#s.recv(1024)
		s.recv(1024)

		s.send(bytes("here , is a another info that is appended"))
		
	except:
		s.close()
		#print("oh it came here!!!! ")
		ip_new_server = "localhost"
		port_new_server = 8049
		s1= socket.socket()
		s1.connect((ip_new_server,port_new_server))


		s1.send(bytes("client"))

		b = s1.recv(1024)
		print("Here is the final info though server1 crashed: ")
		print(b)


		#s1.send(bytes("This is Authentic Client msg. PLease dont reveal to anyone."))

		#m = s1.recv(1024)
		#print(m)
		s1.close()
		break;

