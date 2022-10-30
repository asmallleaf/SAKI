import openpyxl as opx

class XlsxTool():
    def __init__(self):
        self.wb = None
        self.sheetNum = 0
        self.sheet = None
        self.path = None

    def read(self,path):
        if self.__check__(path) == 1:
            self.wb = opx.load_workbook(path)
            self.sheetNum = len(self.wb.sheetnames)
            self.path = path
        else:
            raise Exception('invalidPath')

    def selectSheet(self,sheetName):
        if self.__check__(sheetName,list=self.wb.sheetnames) == 1:
            self.sheet = self.wb[sheetName]
        else:
            raise Exception('invalidPath')

    def save(self,path=None):
        if path is None:
            self.wb.save(self.path)
        else:
            if self.wb is None:
                self.wb = opx.Workbook()
                self.wb.save(path)
            else:
                self.wb.save(path)

    def applyCell(self,start,end,filter):
        pass

    def __strIndex2Int__(self, index):
        colNum = 0
        for i in list(range(0 - len(index), 0)):
            colNum += (ord(index[i]) - 64) * pow(26, (-(i + 1)))
        colNum -= 1
        return colNum

    def __check__(self,val,min=None,max=None,list=None):
        if val is None:
            return 0
        if isinstance(val,int):
            if min is not None and max is not None:
                if val >= min and val <= max:
                    return 1
                else:
                    return 2
        elif isinstance(val,str):
            if list is not None:
                if val in list:
                    return 1
                else:
                    return 3
            else:
                return 1
        return None

if __name__ == '__main__':
    xt = XlsxTool()
    path = r'../testdata/travel-budget.xlsx'
    xt.read(path)
    print(xt.sheetNum)
    xt.selectSheet("test2")
    print(xt.sheet['A1'].value)
    xt.sheet['A1']=3
    path = r'../testdata/test2.xlsx'
    xt.save(path)
