class Student(object):
    def __init__(self,brith,age):
        self.brith = brith
        self.age = age

    @property
    def score(self):
        return self._score
    
    #@score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("wrong type data")
        if value < 0 or value >100:
            raise ValueError("illegal data")
        self._score = value


