import socket
import threading

Host = '127.0.0.1'
Port = 8080

server = socket.socket(socket.AF_INF, socket.SOCK_STREAM)
server.bind(Host, Port)

server.listen()

clients = []
nama = []

#Broadcast pesan */

def broadcast(pesan):
    for client in clients:
        client.send(pesan)

def handle(client):
    while True:
        try:
            pesan = client.recv(1024)
            print(f"{nama[clients.index(client)]} says {pesan}")
            broadcast(pesan)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nama = nama[index]
            nama.remove(nama)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connectdet with{str(address)}!")

        client.send("NAMA".encode('utf-8'))
        nama = client.recv(1024)

        nama.append(nama)
        clients.append(client)

        print(f"Nama Client {nama}")
        broadcast(f"{nama} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server running...")
receive()