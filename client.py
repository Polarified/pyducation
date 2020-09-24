import socket

client = socket.socket()
client.connect(('localhost', 50000))
try:
    while True:
        message = input('> ')
        client.send(message.encode('utf-8'))
        data = client.recv(1024).decode('utf-8')
        print(data)
finally:
    client.close()
