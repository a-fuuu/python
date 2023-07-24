import os
import threading

def foo():
    print('foo: my thread id: ', threading.get_native_id())
    print('foo: my pid is: ', os.getpid())

if __name__ == '__main__':
    print('my pid is: ', os.getpid())
    thread1 = threading.Thread(target = foo).start()
    thread2 = threading.Thread(target = foo).start()
    thread3 = threading.Thread(target = foo).start()
    thread4 = threading.Thread(target = foo).start()  
    # thread 1~4는 하나의 프로세스 안에서 실행되기에 pid는 동일하다 하지만
    # thread는 각기 다르기 때문에 쓰레드 id는 다르다
