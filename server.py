import socket 
import os
s=socket.socket()
port=1634
ip_address=''


s.bind((ip_address,port))
s.listen(20) #listening to 5 client
while(1):
    con,addr = s.accept()
    print("Connection established with client",addr)
    con.send(b"what do u want to do bro! press 1 for timestamp of file or press 2 for transfer file")
    d=con.recv(1024)
    print(d)


    if d==b'1':
        con.send(b'enter the file name you want to know the time stamp')
        file=con.recv(1024)
        time=0
        with open(file) as f:
            time = os.stat("file.txt").st_mtime #to fetch timestamp
            con.send(bytes(str(time),'utf-8'))#sending timestamp
        f.close()        
    if d==b'2':
        con.send(b'enter the file name you want to transfer')
        file=con.recv(1024)
        print(file)
        with open(file, 'wb') as f:
            print('receiving data...')
            data = con.recv(1024)
            f.write(data)
        f.close()
        con.send(b'file transfer sucessfull')
        print("file copied to db")
        
s.close()





