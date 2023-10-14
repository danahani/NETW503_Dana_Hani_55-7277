import socket

def start_server():
    host = "127.0.0.1"   
    port = 54322       

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    print("Server listening on port", port)
    server_socket.listen(1)

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from:", addr)

        handle_client(client_socket)

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')

        if message == "CLOSE SOCKET":
            print("Closing connection")
            client_socket.close()
            break

        response = message.upper()
        client_socket.send(response.encode('utf-8'))

if __name__ == "__main__":
    start_server()
