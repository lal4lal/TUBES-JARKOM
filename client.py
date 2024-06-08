from socket import *
import sys

# Fungsi ini bertanggung jawab untuk mengirim permintaan HTTP GET dan menerima respon dari server.
def request_file(server_hostname, server_port, file_requested):
    # Membuat TCP socket dan koneksi
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_hostname, server_port))
    
    # Membuat dan Mengirim Permintaan HTTP GET
    request = f'GET {file_requested} HTTP/1.0\r\nHost: {server_hostname}\r\n\r\n'
    client_socket.send(request.encode())
    
    # Menerima respon dari server
    response = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        response += chunk
    
    # Menutup Koneksi
    client_socket.close()
    
    # Memisahkan Header dan Body dari Respon
    header_end = response.find(b'\r\n\r\n')
    if header_end != -1:
        header = response[:header_end].decode()
        body = response[header_end + 4:]
    else:
        header = response.decode()
        body = b''
    
    # Mencetak Header dan Body
    print(header)
    if body:
        print(body.decode())

# Penggunaan Skrip dari Baris Perintah
if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <serverhost> <serverport> <filerequested>")
    sys.exit(1)
server_hostname = sys.argv[1]  # Server hostname
server_port = int(sys.argv[2])  # Server port
file_requested = sys.argv[3]  # File requested
    
# Request file ke server dan menampilkan content pada terminal
request_file(server_hostname, server_port, file_requested)