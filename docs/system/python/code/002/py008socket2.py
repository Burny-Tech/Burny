"""
客户端

"""


import  socket

socketClient = socket.socket()

socketClient.connect(("localhost",8888))
while True:
    msg = input("请输入发送信息")
    socketClient.send(f"{msg}".encode('UTF-8'))
    recv_data = socketClient.recv(1024)
    print(f"{recv_data.decode('UTF-8')}")
socketClient.close()