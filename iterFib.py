class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1 #initallize

    def __iter__(self):
        return self #iterate object

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b # next value
        if self.a>10000:
            raise StopIteration()
        return self.a

#test
fi = Fib()
for i in fi:
    print(i)
