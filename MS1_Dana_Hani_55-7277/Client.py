import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5565))

    while True:
        message = input("Enter Your Message: ")
        client.send(message.encode('utf-8'))
        if message == "CLOSE SOCKET":
            client.close()
            break

        response = client.recv(1024).decode('utf-8')
        print(f"Server: {response}")

if __name__ == '__main__':
    start_client()
