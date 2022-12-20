#import required modules
import signal
import socket
import threading

HOST = '127.0.0.1'
PORT = 8080
LISTENER_lIMIT = 5
active_clients = []  #list of all currently connect user


#function to listen for upcoming message from client
def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
        

                final_msg = username + '~' + message 
                send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")

#function to send any new message single clients

def send_message_to_client(client, message):


    client.send(message.encode('utf-8'))

#function to send any new message to all the client that
#are curently connected to this server
def send_messages_to_all(message):

    for user in active_clients:

       user.send(message.encode('utf-8'))
    #    print("kirim pesan ke:",user)

#functioon to handle client
def client_handler(client):
    
    #sever will listen for client message
    while 1:
        
        username = client.recv(2048).decode('utf-8')
        # print("dapet username nih: ",username)
        if username != '':
            
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break

        else:
            print("client username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()

#main function
def main():
    #create the socket class object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    #create a try catch block
    try:
        server.bind((HOST, PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"Unable to bind to host {HOST} and port {PORT}")

    #set server limit
    server.listen(LISTENER_lIMIT)

    #This while loop wil keep listening to client connections
    while 1:

        client, address= server.accept()
        print(f"Successfully connected to client {address[0]} {address[1]}")
        active_clients.append(client)

        threading.Thread(target=client_handler, args=(client, )).start()

        
        
if __name__== '__main__':
    main()




