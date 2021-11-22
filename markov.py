'''
Using markovchain to generate text

'''


import urllib #url扱うlib
import re #正規表現lib
import random #乱数生成lib
import string #文字列扱うlib
import operator #演算子関数扱うlib

class MarkovChain:
    __dic = dict()
    __keyStart = "#start#"
    __keyEnd = "#end#"
    __maxLoop = 100
    __topicMaxLenth = 1000 #文章の長さ

    def __init__(self):
        self.__dic[self.__keyStart]=[]

    def printMarkovChain(self):
        for key in self.__dic.keys():
            print('%s\t%s'%(key,self.__dic[key]))

    def append(self,content): #生成されたmarkovchainに単語追加
        content = re.sub('\s|\n|\t','',content)
        ie = self.getIterator(content)
        i = 0
        for x in ie:
            key ='%s%s'%(x[0],x[1])
            val = x[2]
            if key not in self.__dic.keys():
                self.__dic[key] = []
            self.__dic[key].append(val)
            #記録開始
            if i == 0:
                self.__dic[self.__keyStart].append(key)
            i+=1
        pass

    def getIterator(self,txt):
        ct = len(txt)
        if ct<3:
            return
        for i in range (ct-2+1):
            w1 = txt[i]
            w2 = txt[i+1]
            w3 = txt[i+2] if i+2 < ct else self.__keyEnd
            yield (w1,w2,w3)

    def topicBuilder(self,topicMax=0):
        startKeyArr = self.__dic[self.__keyStart]
        j = random.randint(0,len(startKeyArr)-1)
        key = startKeyArr[j]
        topic = key

        i = 0

        if topicMax <= 0:
            topicMax = self.__topicMaxLenth

        while i < self.__maxLoop:
            i+=1
            if key not in self.__dic.keys():
                break
            arr = self.__dic[key]
            if not arr:
                break
            j = random.randint(0,len(arr)-1)
            if j<0:
                j =0
            sufix = arr[j]
            
            if sufix == self.__keyEnd:
                break
            topic += sufix
            tLen = len(topic)
            if tLen >= topicMax:
                break
            nextKey = '%s%s'%(key[1],sufix)

            if nextKey not in self.__dic.keys():
                break
            key = nextKey
            
        return topic

def fileReader():
    path = r"F:\pproject\text.txt"
    with open(path,'r',encoding='utf-8') as f:
        rows =0
        while True:
            rows += 1
            line = f.readline()
            if not line:
                print('reading finished')
                return
            print('content rows=%s len=%s type=%s'%(rows,len(line),type(line)))
            yield line
    pass

def main():
    markov = MarkovChain()
    reader = fileReader()
    for row in reader:
        print(row)
        markov.append(row)

    for i in range(20):
        topic = markov.topicBuilder(topicMax=300)
        print('%s\t%s'%(i,topic))
    pass

if __name__ == '__main__':
    main()
    pass
