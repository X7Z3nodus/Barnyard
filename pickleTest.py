import pickle
din = dict(name = 'aa', age = 28)
with open('F:\\dump.txt','wb') as fin:
	fin.write(pickle.dumps(din))

with open('F:\\dump.txt','rb') as fout:
	dout = pickle.load(fout)

dout
