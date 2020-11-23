import socket

# creating socket for client
c = socket.socket()

# Here we dont need to bind, thats the server job. Client will simply connect it
# Here we need to pass two things 1.IP address of the server 2.Port number which we want to connect with
c.connect(('localhost',9999))

name=input("Enter your name")
c.send(bytes(name,'utf-8'))

# Now server is sending some data. Its the job of client to accept the data send by the server
# Here we need to mention the size(buffer)
print(c.recv(1024).decode())
