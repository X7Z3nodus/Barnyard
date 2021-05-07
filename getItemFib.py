class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int): #Fib数列を直接生成
            a,b = 1,1
            for x in range(n):
                a,b = b,a+b
            return a
        elif isinstance(n,slice): #sliceとしてパラメータを与えるときsliceのinit&finをゲット
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1

            L=[]
            for x in range(stop):
                if x>= start:
                    L.append(a)
                a,b = b,a+b
            return L
