
import socket 
import os
import time
import signal 

s=socket.socket()
port=8036
ip_address=''

def SigHandler(a,vb):
	print("Exiting..")
	exit(0)	

signal.signal(signal.SIGINT,SigHandler)
c=""
req1=""
req2=""
s.bind((ip_address,port))
s.listen(20) #listening to 5 client
while(1):
    try: 

    	con,addr = s.accept()
    	print("Connection established with client",addr)
    	con.send(b"Hi client, send some information")
    	d=con.recv(1024)
    	print(d) # im ready to send information 

        con.send(bytes("Send contents to save in a file"))

        req = con.recv(1024)   #write

        if(req == "write"):
            with open("demo.txt","w") as f:
                re = con.recv(1024) #Hey, this is client information. 
                f.write(re) 
                print("here is the information from client: ")
                print(re)    #Hey, this is client information. 
                
                '''connecting to server2 for backup'''
                s2 = socket.socket()
        
                s2.connect(("localhost",8049))
                s2.send(bytes("not backup"))
                s2.recv(1024) 
                s2.send(bytes(re))

                backup = s2.recv(1024)  # backup done!!
                s2.close()
    
            f.close()




        con.send(bytes("we recieved your info and uploaded to the file"))

        req1 = con.recv(1024) #append
#      
        con.send(bytes("file to append"))       

        req2 = con.recv(1024)
    	

    except:
    	con.close()
    	s.close()
    	print("except msg, i.e., server1 is crashed")
    	ip_add_server2 = "localhost"
    	s1 = socket.socket()
    	
    	s1.connect((ip_add_server2,8049))
    	
        s1.send(bytes("backup"))
        s1.recv(1024)
        
        s1.send(bytes(req2))

        s1.close()
        break;