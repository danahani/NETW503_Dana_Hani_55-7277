import socket

def start_client():
    host = "127.0.0.1"   
    port = 54322     

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter Your message: ")

        client_socket.send(message.encode('utf-8'))

        if message == "CLOSE SOCKET":
            print("The Connection is Closing")
            client_socket.close()
            break

        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server: {response}")

if __name__ == "__main__":
    start_client()
