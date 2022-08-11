import numpy as np
import pandas as pd

path = r'../testdata/travel-budget.xlsx'
data = pd.read_excel(io=path,header=None)

class ExcelData():
    def __init__(self):
        self.path = None
        self.sheets = None
        self.sheetNum = None
        self.sheetNameList = None
        self.sheet = None
        self.data = None

    def read(self,path=None):
        try:
            self.sheets = pd.read_excel(io=path,header=None,sheet_name=None)
        except FileNotFoundError:
            print('file '+path+' not found')
        except PermissionError:
            print('file '+path+' access limited')
        else:
            self.path = path
            if (isinstance(self.sheets,dict)):
                self.sheetNum = len(self.sheets)
                self.sheetNameList = list(self.sheets.keys())
            else:
                self.sheetNum = 1
        return self.sheets

    def get(self,sheetName=None,sheets=None):
        if sheets is None:
            sheets = self.sheets
        if sheetName is not None:
            if isinstance(sheetName,str):
                if sheetName not in self.sheetNameList:
                    return None
                self.sheet = sheets[sheetName]
                return self.sheet
            elif isinstance(sheetName,int):
                if sheetName>self.sheetNum or sheetName<0:
                    return None
                else:
                    index = self.sheetNameList[sheetName]
                    self.sheet = self.sheets[index]
                    return self.sheet
        else:
            return None

if __name__ == '__main__':
    excel = ExcelData()
    sheets = excel.read(path)
    sheet = excel.get('test2')
    print(sheet)
    print(sheet.values[1,2])