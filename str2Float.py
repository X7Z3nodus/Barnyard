# -*- coding: utf-8 -*-
from functools import reduce

def str2float(s):
    l = s.split('.')
    #print(l)
    return reduce(lambda x,y:x*10+y,map(int,l[0]))+reduce(lambda x,y:x*10+y,map(int,l[1]))/10**len(l[1])

    
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('テスト成功!')
else:
    print('テスト失敗!')
