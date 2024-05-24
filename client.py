from socket import *
import sys

def request_file(server_hostname, server_port, file_requested):
    # Create a TCP/IP socket
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_hostname, server_port))
    
    # Formulate the HTTP GET request
    request = f'GET {file_requested} HTTP/1.0\r\nHost: {server_hostname}\r\n\r\n'
    client_socket.send(request.encode())
    
    # Receive the response from the server
    response = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        response += chunk
    
    # Close the connection
    client_socket.close()
    
    # Split the response into headers and body
    header_end = response.find(b'\r\n\r\n')
    if header_end != -1:
        header = response[:header_end].decode()
        body = response[header_end + 4:]
    else:
        header = response.decode()
        body = b''
    
    # Print the headers and the body
    print(header)
    if body:
        print(body.decode())

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <serverhost> <serverport> <filerequested>")
    sys.exit(1)
server_hostname = sys.argv[1]  # Server hostname
server_port = int(sys.argv[2])  # Server port
file_requested = sys.argv[3]  # File requested
    
# Request the file from the server and print its contents to the terminal
request_file(server_hostname, server_port, file_requested)
