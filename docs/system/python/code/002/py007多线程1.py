"""
一个进程包含多个线程

一个进程内可以运行多个线程,即


import threading

thread_obj = threading.Thread(
[group [,target [,name[,args[,kwargs]]

)

group:暂时没用,未来功能预留参数
target 要执行的任务
args 以元祖的形式给执行任务传参
kwargs 以字典的方式给执行任务传参
name 线程名

#启动线程
thread_obj.start()
"""
import time

import threading


def sing(msg):
    while True:
        print(f"我在唱歌{msg}")
        time.sleep(1)


def dance():
    while True:
        print("我在跳舞")
        time.sleep(1)


if __name__ == '__main__':
    # sing()
    # dance()
    # 这里要注意,哪怕只有一个参数也是需要加逗号
    t1 = threading.Thread(target=sing,args=("参数11",), name="多线程唱歌")
    t2 = threading.Thread(target=dance, name="多线程跳舞")
    t1.start()
    t2.start()
