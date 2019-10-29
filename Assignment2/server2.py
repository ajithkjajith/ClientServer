import socket 
import os
import time
import signal 

s2=socket.socket()
port=8049
ip_address=''

s2.bind((ip_address,port))
s2.listen(20) #listening to 5 client


def SigHandler(a,vb):
	print("Exiting..")
	exit(0)	

while(1):
    con,addr = s2.accept()
    res = con.recv(1024) #not backup  #for second time is backup
    if(res == "backup"):
        with open("demo_backup.txt","a") as f:
            con.send(bytes("backup recv"))
            info = con.recv(1024)
            print("server 1 is crashed:")
            print(info)
            f.write(info)
            f.close()
            print("append done in server2")


        # with open("demo_backup.txt","r") as f:
        #     rd = f.read(1024)
        #     con.send(bytes(rd))
        #     f.close()

    elif(res=="client"):
        with open("demo_backup.txt","r") as f:
            rd = f.read(1024)
            con.send(bytes(rd))
            f.close()
      
    else:
        with open("demo_backup.txt","w") as f:
            con.send(bytes("yes recv"))
            info = con.recv(1024)  #hey, this is client information
            print("first time backup:")
            print(info)
            f.write(info)

            f.close()

    con.close()
s2.close()