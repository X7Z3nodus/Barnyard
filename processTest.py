from multiprocessing import Process
import os

url = 'F:\\log.txt'
def processTest(name):
    with open(url,'a') as f:
        f.write('Run child process %s (%s) \n ' %(name, os.getpid()))


if __name__ == '__main__':
    with open(url,'w') as f:
        f.write('parent process %s \n'% os.getpid())
    p = Process(target=processTest, args=('test',))
    with open(url,'a') as f:
        f.write('Child process will start. \n')
    p.start()
    p.join()
    with open(url,'a') as f:
        f.write('Child process end. \n')
