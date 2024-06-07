from socket import *
import sys

def minta_file(nama_server, port_server, file_diminta):
    # Buat socket TCP/IP
    socket_klien = socket(AF_INET, SOCK_STREAM)
    socket_klien.connect((nama_server, port_server))
    
    # Formulasikan permintaan HTTP GET
    permintaan = f'GET {file_diminta} HTTP/1.0\r\nHost: {nama_server}\r\n\r\n'
    socket_klien.send(permintaan.encode())
    
    # Terima respons dari server
    respons = b''
    while True:
        chunk = socket_klien.recv(1024)
        if not chunk:
            break
        respons += chunk
    
    # Tutup koneksi
    socket_klien.close()
    
    # Pisahkan respons menjadi header dan body
    akhir_header = respons.find(b'\r\n\r\n')
    if akhir_header != -1:
        header = respons[:akhir_header].decode()
        body = respons[akhir_header + 4:]
    else:
        header = respons.decode()
        body = b''
    
    # Cetak header dan body
    print(header)
    if body:
        print(body.decode())

if len(sys.argv) != 4:
    print(f"Usage: {sys.argv[0]} <nama_server> <port_server> <file_diminta>")
    sys.exit(1)
nama_server = sys.argv[1]  # Nama server
port_server = int(sys.argv[2])  # Port server
file_diminta = sys.argv[3]  # File yang diminta
    
# Minta file dari server dan cetak isinya ke terminal
minta_file(nama_server, port_server, file_diminta)
