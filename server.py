import socket

def main():
    host = input("Masukkan Host: ")
    port = int(input("Masukkan Port: "))

    # Membuat socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mengikat socket ke host dan port yang ditentukan
    server_socket.bind((host, port))

    # Mendengarkan koneksi yang masuk, maksimal 1 koneksi dalam antrean
    server_socket.listen(1)
    print(f"Server berjalan di {host}:{port}")

    try:
        while True:
            # Menerima koneksi dari klien
            client_socket, client_address = server_socket.accept()
            print(f"Terhubung dari {client_address}")

            # Mengirimkan pesan ke klien
            message = "Halo dari server!"
            client_socket.sendall(message.encode('utf-8'))

            # Menutup koneksi dengan klien
            client_socket.close()
            print(f"Koneksi dengan {client_address} ditutup")
    finally:
        # Menutup socket server jika ada kesalahan atau server dimatikan
        server_socket.close()

if __name__ == "__main__":
    main()
