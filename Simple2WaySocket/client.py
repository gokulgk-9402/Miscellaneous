import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

connected = True

def send():
    global connected
    while connected:
        msg = input("Enter message to send: \n")
        message = msg.encode(FORMAT)
        
        client.send(message)
        print(msg == DISCONNECT_MESSAGE)
        if msg == DISCONNECT_MESSAGE:
            connected = False

def recv():
    global connected
    while connected:
        msg = client.recv(2048).decode(FORMAT)
        if msg:
            print(f"\nServer: {msg}\n")
            if connected:
                print("Enter message to send: ")

print("Connected to server!")

send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=recv)

send_thread.start()
recv_thread.start()

send_thread.join()
recv_thread.join()