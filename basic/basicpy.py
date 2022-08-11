from abc import abstractmethod
class Tut(object):
    def __init__(self):
        print("this is basic python language tutorial!!")

    @abstractmethod
    def show(self):
        pass

class IntTut(Tut):
    def __init__(self):
        self.numi = 2
        self.numf = 3.14

    def show(self):
        tips = "A Integer Num: "+str(self.numi)
        print(tips)
        tips = "A Float Num: "+str(self.numf)
        print(tips)
        tips = "do some calculation, like multiple: "+str(self.numi*self.numf)
        print(tips)

class StringTut(Tut):
    def __init__(self):
        self.fname = 'Weng'
        self.lname = 'Xisong'

    def show(self):
        tips = "my first name is "+self.fname
        print(tips)
        tips = "I'm "+self.fname+' '+self.lname
        print(tips)

class ListTut(Tut):
    def __init__(self):
        self.list = [1]

    def show(self):
        tips = 'list A:'
        print(tips)
        print(self.list)
        self.list = [2, self.list]
        self.list.append(1)
        print(tips)
        print(self.list)
        self.list.pop()
        print(tips)
        print(self.list)
        self.list = list(range(5))
        tips = 'list B[:]: '
        print(tips)
        print(self.list)
        tips = 'list B[1:-2]'
        print(tips)
        print(self.list[1:-2])
        tips = "[1:-2] is actually [2, -2)"
        print(tips)

class DicTut(Tut):
    def __init__(self):
        self.dict = {'1':1}

    def show(self):
        tips = 'a dictionary is like: '
        print(tips)
        print(self.dict)
        tips = "we can search by key, such as dict['1']"
        print(tips)
        print(self.dict['1'])
        tips = 'we can print all keys'
        print(tips)
        print(self.dict.keys())
        tips = 'or values'
        print(tips)
        print(self.dict.values())
        tips = "add a set of values, such as dict['2']=2 "
        self.dict['2'] = 2
        print(tips)
        print(self.dict)
        tips = "delete a set of values, such as dict.pop('2')"
        self.dict.pop('2')
        print(tips)
        print(self.dict)
        tips = "Actually, we can also change list or tuple into dict, such as dict=[('1',1),('2',2)]"
        self.dict = [('1',1),('2',2)]
        print(tips)
        print(self.dict)

class MapTut(Tut):
    def __init__(self):
        self.map = {1,'a',1,2}

    def show(self):
        tips = 'a map or set is like'
        print(tips)
        print(self.map)
        tips = 'it is actually a set, which means a set of {1,2,2,1} will be'
        print(tips)
        print({1,2,2,1})
        tips = 'use discard to remove a value, remove is also ok but it may leads to error'
        print(tips)
        tips = 'update a value by map.update([3])'
        print(tips)
        self.map.update([3])
        print(self.map)


def enter(tut):
    tut.show()

welcome = Tut()
intTut = IntTut()
strTut = StringTut()
listTut = ListTut()
dicTut = DicTut()
mapTut = MapTut()

if __name__ == "__main__":
    enter(mapTut)