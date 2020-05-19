import socket


# create an INET (i.e. IPv4), STREAMing socket
browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
browser_socket.connect(("google.com", 80))

# Get socket name
print("Socket Name:", browser_socket.getsockname())
# Get peer name
print("Peer Name:", browser_socket.getpeername())
# Get timeout
print("Timeout:", browser_socket.gettimeout())

