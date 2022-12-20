import datatool2 as dt2
import sqltool as st

class FIA():
    def __init__(self):
        self.dt = dt2.XlsxTool()
        self.st = st.sqltool()
        self.signals = None
        self.tableName = 'Safety Signals'
        self.dbTable = None
        self.sfSignals = None

    def loadDB(self,path):
        self.dt.read(path)
        self.dt.selectSheet('PCB_MsgSig')
        dbTable = DBTable()
        dbTable.signal = self.dt.extract(self.dt.sheet['E'])
        dbTable.signal[0]=[]
        dbTable.id = self.dt.extract(self.dt.sheet['B'])
        dbTable.id[0]=[]
        dbTable.message = self.dt.extract(self.dt.sheet['A'])
        dbTable.message[0]=[]
        dbTable.shortName = self.dt.extract(self.dt.sheet['F'])
        dbTable.shortName[0]=[]
        dbTable.data=self.dt.extract(self.dt.sheet['L'])
        dbTable.shortName[0]=[]
        self.dt.selectSheet('PCB_Tx')
        dbTable.period = self.dt.extract(self.dt.sheet['E'])
        dbTable.period[0] = []
        dbTable.tx = self.dt.extract(self.dt.sheet['A'])
        dbTable.tx[0] = []
        dbTable.rx = self.dt.extract(self.dt.sheet['B'])
        dbTable.rx[0] = []
        self.dbTable = dbTable

    def loadSS(self,path,SheetName,col):
        self.dt.read(path)
        self.dt.selectSheet(SheetName)
        self.sfSignals = self.dt.extract(self.dt.sheet[col])
        self.sfSignals = list(set(self.sfSignals))



class DBTable():
    def __init__(self):
        id = st.TableTitle('id','TEXT',False,True)
        signal  = st.TableTitle('signal','TEXT',False,False)
        message = st.TableTitle('message','TEXT',False,False)
        shortName = st.TableTitle('shortName''TEXT',False,False)
        data = st.TableTitle('data','TEXT',False,False)
        period = st.TableTitle('period','TEXT',False,False)
        tx = st.TableTitle('tx','TEXT',False,False)
        rx = st.TableTitle('rx','TEXT',False,False)
        self.titles = [id,signal,message,shortName,data,period,tx,rx]
        self.tableName = 'Database'
        self.id = None
        self.signal = None
        self.message = None
        self.shortName = None
        self.data = None
        self.period = None
        self.tx = None
        self.rx = None


if __name__ == '__main__':
    fia =FIA()
    fia.loadDB(r'..\testdata\test2.xlsx')
    fia.dt.selectSheet('test2')
    print(fia.dt.sheet['A'])