import socket

def main():
    host = input("Masukkan Host: ")
    port = int(input("Masukkan Port: "))

    # Membuat socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Menghubungkan socket ke server
        client_socket.connect((host, port))

        # Menerima pesan dari server
        received_data = client_socket.recv(1024)
        print("Balasan dari server:", received_data.decode('utf-8'))
    finally:
        # Menutup koneksi dengan server
        client_socket.close()

if __name__ == "__main__":
    main()
