from socket import *
import mimetypes


def handle_client(client_connection):
    request = client_connection.recv(1024).decode()
    print(request)
    # Memisahkan header per baris
    headers = request.split('\n')
    # Mengambil file yang diminta yang ada pada header
    # pada baris pertama setelah request method
    file_requested = headers[0].split()[1]
    # index.html sebagai default saat server dijalankan
    if file_requested == '/':
        file_requested = '/index.html'
    try:
        # Membuka file yang diminta oleh klien
        with open('./data/'+file_requested, 'rb') as file:
            content = file.read()

        # Mengambil content-type dari request klien
        content_type, _ = mimetypes.guess_type(file_requested)
        # Membuat response header dengan kode 200 OK dan tipe content
        response_header = f'HTTP/1.0 200 OK\nContent-Type: {content_type}\n\n'.encode()
        client_connection.send(response_header + content)
    except FileNotFoundError:
        # Error Handling jika file yang direquest tidak ditemukan
        response_header = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'.encode()
        response_content = b''
        client_connection.send(response_header + response_content)
    client_connection.close()

def run_server(server_hostname, server_port):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((server_hostname, server_port))
    serverSocket.listen(1)
    print(f'[*] Listening on {server_hostname}:{server_port}...')
    while True:
        client_connection, client_address = serverSocket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        handle_client(client_connection)

def main():
    server_hostname = 'localhost'
    server_port = 7070 
    
    # Memulai server dengan host dan port yang ditentukan
    run_server(server_hostname, server_port)

# Memanggil fungsi main
main()
