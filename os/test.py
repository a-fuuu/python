from multiprocessing import Process
import os

def foo():
    print('foo: child process: ', os.getpid())
    print('foo: parent process: ', os.getppid()) # ppid는 parent process pid

def bar():
    print('bar excuted!')

def baz():
    print('baz excuted!')

if __name__ == '__main__':
    print('parent process', os.getpid())
    child = Process(target=foo).start()
    child1 = Process(target=foo).start()
    child2 = Process(target=foo).start()

    child3 = Process(target=bar).start()
    child4 = Process(target=baz).start()
    # child 1~3의 부모는 같다 따라서 ppid 또한 동일할 것
