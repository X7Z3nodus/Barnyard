import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('log: call %s()' %func.__name__)
        return(func(*args,**kw))
    return wrapper

@log
def now():
    print('hello')
@log
def well():
    print('Hi')
@log
def test2():
    print('Hallo')
