import socket
import time
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '127.0.0.1'
host = '20.211.33.233'
port = 65432
client.connect((host, port))

while True:
    # random choose an acton from '1','2','3'
    sendMsg = str(random.randint(1, 3))
    # send the request to the server
    client.send(sendMsg.encode("utf-8"))
    sendMsg = sendMsg + '\n'
    print('request: ' + sendMsg)
    time.sleep(3)
    # receive message from server
    msg = client.recv(1024)
    print('Server: ' + msg.decode("utf-8"))
# close client
client.close()
