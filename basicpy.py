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
        tips = ''

def enter(tut):
    tut.show()

welcome = Tut()
intTut = IntTut()
strTut = StringTut()
listTut = ListTut()

if __name__ == "__main__":
    enter(listTut)