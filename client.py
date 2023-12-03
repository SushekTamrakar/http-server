import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect('127.0.0.1', 9000)
cmd = 'GET http://127.0.0.0.1/test.txt hTTP/1,0\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')