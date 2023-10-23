import socket
import threading

clients = []

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if data == "CLOSE SOCKET":
            clients.remove(client_socket)
            client_socket.close()
            break
        else:
            client_socket.send(data.upper().encode('utf-8'))

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5565))
    server.listen(5)
    print("[*] Server listening on port 5565")

    while True:
        client_socket, _ = server.accept()
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    start_server()
