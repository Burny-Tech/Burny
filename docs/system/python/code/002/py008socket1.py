"""

服务端:等待其他进程的链接,可接收发来的消息,可以回复消息
客户端:主动链接服务端,可以发送消息,可以接收消息

"""

import socket

socketserver = socket.socket()
# 绑定主机 和端口号
socketserver.bind(("127.0.0.1",8888))
# 表示允许的链接数据量超出会等待,可以不填,不填会自动设置一个合理的值
socketserver.listen(10)
# accept 方法是阻塞,如果没有连接,会卡在当前这一行,不会向下执行代码
# accept 返回的是一个二元元祖,可以使用上述形式,用两个变量接收二元元祖的2 个元素

conn, address = socketserver.accept()

print({address})


# 客户端连接后,通过recv方法,接收客户端发送的消息

# while True:
#     data = conn.recv(1024).decode("UTF-8")
#     # recv 方法的返回值是字节数组 (Bytes) 可以通过decode 使用UTF-8 解码为字符串
#     # recv 方法的传参是 buffsize ,缓冲区大小,一般设置为1024 即可
#     if  data == 'exit':
#         break
#     print(f"接收到的数据{data}")

# 可以通过while True  无线循环来持续和客户端进行数据交互
# 可以通过判定客户端发来的特水标记,如 exit 退出无限循环

# 第六步
"""
通过 conn 客户端档次连接对象,调用send 方法可以回复消息
"""
while True:
    data:  str  = conn.recv(1024).decode("UTF-8")
    print(f"服务端接收客户端的数据{data}")
    msg= input("请输入回复的消息")
    conn.send(f"{msg}".encode("UTF-8"))

# 第七步:
"""
connn 客户端档次拦截对象 和 socket_server 对象调用close 方法,关闭连接

"""
conn.close()
socketserver.close()