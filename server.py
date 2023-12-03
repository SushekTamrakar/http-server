import socket
import threading


HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE=  "******** CONNECTION LOST *******************"

ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # For IPV6 addresses AF_INET

server.bind(ADDR)

def handle_client(conn, addr):
    print("New connection----------------")
    print(addr, ' - conected')

    conncted = True

    while conncted:
        message_length = conn.recv(HEADER).decode(FORMAT)
        if message_length:
            message_length = int(message_length)
            msg = conn.recv(message_length).decode(FORMAT)
            print(addr, '-', msg)
            if msg == DISCONNECT_MESSAGE:
                conncted = False

            print(f"[{addr}] {msg}")
            conn.send("message recieved".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print("Server is Listening on ", SERVER)
    while True:
        conn, addr = server.accept() #conn is connection that we ginna send the information back and addr is the information about the cinnection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        active_connection = threading.active_count() - 1
        print("Active Connection ", active_connection)


print("Server is starting.....................")
start()






# def createServer():
#     serversocket = socket(AF_INET, SOCK_STREAM)

#     try:
#         serversocket.bind(('localhost', '9000'))
#         serversocket.listen(5)

#         while(1):
#             (clientsocket, address) = serversocket.accept()
#             rd = clientsocket.recv(5000).decode()
#             pieces = rd.split("\n")
#             if ( len(pieces)> 0) : print(pieces[0])

#             data = "HTTP/1.1 200 OK \r\n"
#             data += "Content-Type: text/html; charset=utf-8\r\n"
#             data += '\r\n'
#             data += "<html><body>Hello World</body></html>\r\n\r\n"
#             clientsocket.sendall(data.encode())
#             clientsocket.shutdown(SHUT_WR)


#     except KeyboardInterrupt :
#         print("\nShutting Down...\n")

#     except Exception as exc :
#         print("Error")
#         print(exec)

#     serversocket.close()

# print('Access https://localhost:9000')
# createServer() 