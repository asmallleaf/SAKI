import sqlite3 as sql

class SqlTool():
    def __init__(self):
        self.db = None
        self.cur = None
        self.debug = False

    def connect(self,dbName):
        self.db = sql.connect(dbName)
        self.cur = self.db.cursor()
        if self.debug is True:
            print('database open successfully')

    def table(self,name,titles):
        script = 'CREATE TABLE ' + name+'(\n'
        num = len(titles)
        for i in range(0,num):
            if i < (num-1):
                script += titles[i].make() + ',\n'
            else:
                script += titles[i].make() + '\n'
        script+=');'
        self.cur.execute(script)
        self.db.commit()
        if self.debug is True:
            print('table '+name+' create successfully')

    def insert(self,tableName,values):
        subScript = 'INSERT INTO '+tableName+' VALUES ('
        script = ''
        for value in values:
            script += subScript + value + ');\n'
        print(script)
        self.cur.executescript(script)
        self.db.commit()
        if self.debug is True:
            print('insert successfully')

    def delete(self,tableName,conditions):
        subScript = 'DELETE FROM '+tableName+' where '
        script = ''
        for condition in conditions:
            script += subScript+condition+';\n'
        self.cur.executescript(script)
        self.db.commit()
        if self.debug is True:
            print('delete successfully')

    def select(self,tableName,cols):
        if len(cols) > 1:
            script = 'SELECT '+','.join(cols)+ ' FROM '+tableName+';'
        else:
            script = 'SELECT '+ cols[0] + ' FROM '+tableName+';'
        self.cur.execute(script)
        self.db.commit()
        if self.debug is True:
            print('query successfully')
        return self.cur

    def close(self):
        self.db.close()

class TableTitle():
    def __init__(self,name='',type='',nullable=True,primaryKey=False):
        self.name = name
        self.type = type
        if nullable is True:
            self.null = ''
        else:
            self.null = 'NOT NULL'
        if primaryKey is False:
            self.primaryKey = ''
        else:
            self.primaryKey = 'PRIMARY KEY'
        self.title = ''

    def make(self):
        self.title = ' '.join([self.name,self.type,self.primaryKey,self.null])
        return self.title

class Table():
    def __init__(self):
        self.tableName = None
        self.titles = None
        self.vals = None
def table2sql(table,db):
    st = SqlTool()
    st.connect(db)
    st.table(table.tableName,table.titles)
    st.insert(table.tableName,table.vals)
    st.close()


if __name__ == '__main__':
    sex = TableTitle('sex','TEXT','','')
    sqltool = SqlTool()
    testdb = sqltool.connect('../testdata/testdb.db')
    #sqltool.table('testtb',[sex])
    sqltool.insert('testtb',['\'male\''])
    #sqltool.delete('testtb',['sex = \'male\''])
    rows = sqltool.select('testtb',['sex'])
    for row in  rows:
        print(row[0])
