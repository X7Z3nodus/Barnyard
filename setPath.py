class setPath(object):

    def __init__(self,path=''): #init:空白パス
        self._path = path

    def __getattr__(self,path): #パラメータをパスの一部分として追加
        return setPath('%s/%s' % (self._path,path)) 

    def __call__(self,path): #objを直接呼び出して、パラメータをパスの一部分として追加
        return setPath('%s/%s' % (self._path,path))

    def __str__(self):
        return self._path

    __repr__ = __str__


url = setPath().User('X7').lib
'''
equal
url = setPath()
url.user
url = user('X7')
url.lib
'''
