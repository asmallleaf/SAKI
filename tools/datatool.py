import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import openpyxl as opl
import xlsxwriter

class ExcelData():
    def __init__(self):
        self.path = None
        self.sheets = None
        self.sheetNum = None
        self.sheetNameList = None
        self.sheet = None
        self.data = None
        self.col = None
        self.row = None
        self.rowNum = 0
        self.colNum = 0
        self.sheetName = None

    def read(self,path=None):
        try:
            if '.xlsx' in path:
                self.sheets = pd.read_excel(io=path,header=None,sheet_name=None)
            elif '.csv' in path:
                self.sheets = pd.read_csv(path,header=None)
        except FileNotFoundError:
            print('file '+path+' not found')
        except PermissionError:
            print('file '+path+' access limited')
        else:
            self.path = path
            if (isinstance(self.sheets,dict)):
                self.sheetNum = len(self.sheets)
                self.sheetNameList = list(self.sheets.keys())
                if self.sheetNum == 1:
                    self.sheet = self.sheets[self.sheetNameList[0]]
                    [self.rowNum, self.colNum] = self.sheet.shape
            else:
                self.sheetNum = 1
                self.sheetNameList = [0]
                self.sheet = self.sheets
                [self.rowNum,self.colNum] = self.sheet.shape
        return self.sheets

    def getSheet(self,sheetName=None,sheets=None):
        if sheets is None:
            sheets = self.sheets
        if sheetName is not None:
            if isinstance(sheetName,str):
                if sheetName not in self.sheetNameList:
                    print('sheet name not exist')
                    return None
                self.sheet = sheets[sheetName]
                self.sheetName = sheetName
                return self.sheet
            elif isinstance(sheetName,int):
                if sheetName>self.sheetNum or sheetName<0:
                    print('sheet number out of range')
                    return None
                else:
                    index = self.sheetNameList[sheetName]
                    self.sheet = self.sheets[index]
                    self.sheetName = self.sheetNameList[sheetName]
                    return self.sheet
        else:
            return None

    def __set__(self,sheet=None,row=None,col=None):
        if sheet is not None:
            self.sheet = sheet
        if row is not None:
            self.row = row
        if col is not None:
            self.col = col

    def filterNan(self,list=None):
        if list is None:
            return None
        length = len(list)
        for x in list(range(0,length)):
            if list[x] == 'NaN':
                list.pop(x)
        return list

    def getRow(self,rownum,sheet=None):
        if self.__checkRange__(rownum=rownum) is False:
            return None
        return self.sheet.values[rownum,:]
    def getCol(self,colnum):
        isTrue = self.__checkRange__(colnum=colnum)
        if isTrue is False:
            return None
        elif isTrue == 2:
            colnum = self.__strIndex2Int__(colnum)
        return self.sheet.values[:,colnum]

    def getCell(self,rownum,colnum):
        isTrue = self.__checkRange__(rownum,colnum)
        if isTrue is False:
            return None
        elif isTrue == 2:
            colnum = self.__strIndex2Int__(colnum)
        return self.sheet.values[rownum,colnum]

    def __strIndex2Int__(self,index):
        colNum = 0
        for i in list(range(0-len(index),0)):
            colNum += (ord(index[i])-64)*pow(26,(-(i+1)))
        colNum -= 1
        return colNum

    def __checkRange__(self,rownum=None,colnum=None):
        [maxRowNum, maxColNum] = self.sheet.shape
        isTure = False
        if rownum is not None:
            if isinstance(rownum,int):
                if rownum >= maxRowNum or rownum < 0:
                    print('row num out of range')
                    isTure = False
                else:
                    isTure = True
            else:
                print('row index is not valid')
                isTure = False
        if colnum is not None:
            if isinstance(colnum,str):
                colnum = self.__strIndex2Int__(colnum)
                if colnum >= maxColNum or colnum < 0:
                    print('col index out of range')
                    isTure = False
                else:
                    isTure = 2
            elif isinstance(colnum,int):
                if colnum >= maxColNum or colnum < 0:
                    print('col index out of range')
                    isTure = False
                else:
                    isTure = 1
            else:
                print('col index is not valid')
                isTure = False
        return isTure

    def makeHeader(self,rowList=None,colList=None):
        header = []
        if rowList is None and colList is not None:
            for col in colList:
                if self.__checkRange__(colnum=col) is False:
                    return None
                elif self.__checkRange__(colnum=col) == 2:
                    col = self.__strIndex2Int__(col)
                header.extend(self.getCol(colnum=col))
        elif colList is None and rowList is not None:
            for row in rowList:
                if self.__checkRange__(rownum=row) is False:
                    return None
                header.extend(self.getRow(rownum=row))
        elif colList is None and rowList is None:
            return None
        else:
            for col in colList:
                if self.__checkRange__(colnum=col) is False:
                    return None
                elif self.__checkRange__(colnum=col) == 2:
                    col = self.__strIndex2Int__(col)
            for row in rowList:
                if self.__checkRange__(rownum=row) is False:
                    return None
            for col in colList:
                for row in rowList:
                    header.append(self.getCell(rownum=row,colnum=col))
        return header

    def collect(self,rowIndex=None,colIndex=None,rowList=None,colList=None):
        rowNum = len(rowList)
        colNum = len(colList)
        rowi = 0
        coli = 0
        data = np.zeros((rowNum,colNum))
        for col in colList:
            for row in rowList:
                data[rowi][coli]=self.getCell(row,col)
                rowi+=1
            rowi = 0
            coli+=1
        collection = pd.DataFrame(data=data,index=rowIndex,columns=colIndex)
        return collection

    def setCell(self,rowIndex=None,colIndex=None,val=None):
        #isTrue = self.__checkRange__(rowIndex,colIndex)
        #if isTrue is False:
        #    return None
        #elif (isTrue==2):
        #    colIndex = self.__strIndex2Int__(colIndex)
        self.sheet.values[rowIndex,colIndex] = val
    def makeExcel(self,path=None):
        if path is None:
            path = self.path
        with pd.ExcelWriter(path,engine='xlsxwriter') as writer:
            self.sheet.to_excel(writer,sheet_name=self.sheetName,index=False,header=False)

class DrawData():
    def __init__(self):
        self.data = None
        self.title = None
        self.labels = None
        self.typeList = {'线形图':'line','柱状图':'bar','水平柱状图':'barh','组合柱状图':'bar','堆叠柱状图':'bar','饼图':'pie','散点图':'scatter','直方图':'hist','箱体图':'box','面积图':'area'}
        self.kind = 'line'
        self.__rcSet__()

    def show(self,data=None,kind='线形图'):
        if self.__typeMap__(kind) is None:
            print('the graph type is not found')
            return None
        data.plot(kind=self.kind)
        mpl.show()

    def __rcSet__(self):
        mpl.rc('font',family='Youyuan',size=11)
        mpl.rc('axes',unicode_minus='False')

    def __typeMap__(self,typeStr=None):
        if typeStr is None:
            return None
        if isinstance(typeStr,str):
            if typeStr in self.typeList.keys():
                self.kind = self.typeList[typeStr]
                return self.kind
            else:
                return None
        else:
            return None

if __name__ == '__main__':
    path = r"../testdata/test.xlsx"
    excel = ExcelData()
    draw = DrawData()
    excel.read(path)
    #header = excel.makeHeader(rowList=[0])
    #td = excel.collect(colIndex=header,rowList=list(range(1,10)),colList=list(range(0,4)))
    #print(td.values)
    #draw.show(td)

    excel.getSheet('Sheet1')
    excel.setCell(1,1,0)
    excel.makeExcel()