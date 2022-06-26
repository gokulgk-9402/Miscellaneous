import socket 
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

connected = True
number = 0

def send(conn, addr):
    global connected
    while connected:
        msg = input("Enter message to send: \n")
        conn.send(msg.encode(FORMAT))

def recv(conn, addr):
    global connected, number
    while connected:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
            if msg == DISCONNECT_MESSAGE:
                connected = False
                conn.send("Disconnected".encode(FORMAT))
                print(f"{addr} Disconnected.")
                number -= 1
                print(f"ACTIVE CONNECTIONS: {number}")

            print(f"\n{addr}: {msg}\n")
            print("Enter message to send: ")

def handle_client(conn, addr):
    global connected
    print(f"{addr} connected.")

    connected = True
    send_thread = threading.Thread(target=send, args = [conn, addr])
    recv_thread = threading.Thread(target=recv, args = [conn, addr])

    send_thread.start()
    recv_thread.start()

    send_thread.join()
    recv_thread.join()
    

    conn.close()
        

def start():
    global number
    server.listen()
    print(f"Server is listening on {SERVER}...")
    while True:
        conn, addr = server.accept()
        number += 1
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"ACTIVE CONNECTIONS: {threading.active_count() - 1}")


print("Server is starting...")
start()