#fib

def fib(num):
    n,a,b = 0,0,1
    while n<=num:
        yield b
        a,b = b,a+b
        '''
        t = (b,a+b) #防止a中途出现值的变化
        a = t(0)
        b = t(1)
        '''
        n = n+1
    return 'done'

