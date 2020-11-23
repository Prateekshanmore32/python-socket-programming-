import socket
# s=Server socket
# Here we need to pass two parameters 1.Type of Protocol(IPV4/V6)  2.Type of network(TCP/UDP)
# By default it is IPV4(Protocol) and TCP(Type of Network)
s = socket.socket()
print("Socket Created")

# we are making this socket as a server socket so it will accept the connection
# But if we want to accept the connection we will be having the IP address so we need port number
# we need to bind the socket and the port address
# Range of the port number is 0-65535
# Here we need to pass two parameters 1. IP address(we will be using the same machine) 2. Port number
s.bind(('localhost',9999))

# Now the next step is to start listening to the clients-/740
# Here making 3 connection (listening to 3 clients)
s.listen(3)

print("waiting for the connection")

# so now we are continously listening to the clients and hence using the while loop
while True:
    # In this we need to accept the connection
    # It will give you two things 1.client socket(c) and address of the client
    c, addr= s.accept()
    name=c.recv(1024).decode()
    print("Connected with",addr,name)
    c.send(bytes('Hi Im Prateeksha','utf-8'))
    c.close()

