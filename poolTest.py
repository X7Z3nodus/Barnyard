from multiprocessing import Pool
import time, os, random

def taskRandomTime(name):
    print('Run Task %s (%s)...' % (name, os.getpid()))
    start = time.time()  # get start time
    time.sleep(random.random() * 3)  # subprocess sleep
    end = time.time()
    print('Task %s run %0.2f sec.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % (os.getpid()))
    p = Pool(3)
    for i in range(4):
        p.apply_async(taskRandomTime, args=(i,))  # asynchronize create subprocess
    print('Waiting all subprocesses done...')
    p.close()
    p.join()
    print('All has been done')
