# -*- coding: utf-8 -*-
class Screen(object):
    @property
    def width(self):
        return self._width 
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('wrong tpye number')
        self._width = value

    @property
    def height(self):
        return self._height 
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('wrong tpye number')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('success!')
else:
    print('fall!')
