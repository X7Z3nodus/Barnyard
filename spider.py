from urllib import request

with request.urlopen('https://portal.i.meitec.com/group/fiels/') as f:
    print(f.info())
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
