import pymssql
import pandas as pd

class Database:
    def __init__(self, host="10.11.145.141:1433",user='sa',password='Mascot123'):
        '''
        param host: str
                数据库地址
        param user: str
                用户名
        param password: str
                密码
        '''
        self.host = host
        self.user = user
        self.password = password
    def connect_sql(self):
        '''连接sql server'''
        # 连接本地sql server         地址          用户名   密码
        self.conn = pymssql.connect(self.host, self.user, self.password) # 连接sql server
        
        
    def connect_db(self,database:str):
        '''
        连接数据库
        param database: str
                数据库名
                
        '''
        try:
            # 连接本地sql server         地址          用户名   密码     数据库
            self.conn = pymssql.connect(self.host, self.user, self.password, database)
        except:
            print("数据库连接失败")
    def close(self):
        '''关闭连接'''
        self.conn.close()
        
    def create_db(self,database:str):
        '''创建数据库
        
        param database: str
                数据库名

        '''
        self.connect_sql()
        cursor = self.conn.cursor() # 创建游标
        self.conn.autocommit(True)   #指令立即执行，无需等待conn.commit()
        sql = "CREATE DATABASE %s "%database

        cursor.execute(sql) # 执行sql语句
        self.conn.autocommit(False) # 关闭自动提交    
        self.close() # 关闭连接
        
    def delect_db(self,database:str):
        self.connect_sql()
        cursor = self.conn.cursor() # 创建游标
        self.conn.autocommit(True)   #指令立即执行，无需等待conn.commit()
        sql = "DROP DATABASE %s "%database
        
        cursor.execute(sql) # 执行sql语句
        self.conn.autocommit(False) # 关闭自动提交
        self.close()  # 关闭连接
    
    def create_table(self,database:str,table_name:str,table_head:str,primary_key=None):
        '''
        创建表
        
        param database: str
                 数据库名
        param table_name:str
                表名
        param table_head:str
                表头
        param primary_key: str
                主键(默认为None)
        '''
        
        if type(table_head)!=list:
            raise Exception("表头必须为list类型")
            return
        head='' #表头
        for i in range(len(table_head)):
            head+=table_head[i]+' VARCHAR(100),' #表头
        head=head[:-1]
        if primary_key!=None: #如果有主键   
            head+=',PRIMARY KEY(%s)'%primary_key # 添加主键
            
        self.connect_db(database)
        cursor = self.conn.cursor()   
      
        cursor.execute("""
            IF OBJECT_ID('%s', 'U') IS  NULL
            CREATE TABLE %s (
                %s )
            """%(table_name,table_name,head))
        self.conn.commit() # 提交
        self.close() # 关闭连接
    def delect_table(self,database,table_name):
        '''
        删除表
        param database: str
                数据库名
        param table_name: str
                表名 
                    
        '''
        self.connect_db(database)
        cursor = self.conn.cursor()     
        cursor.execute("""
            IF OBJECT_ID('%s', 'U') IS NOT NULL
            DROP TABLE %s
            """%(table_name,table_name))
        self.conn.commit() # 提交
        self.close() # 关闭连接
    
    def add_column(self,database,table_name,column_name,column_type='VARCHAR(100)'): #添加列
        ''' 
        添加列
        
        param database: str
                数据库名
        param table_name: str
                表名
        param column_name: str
                列名
        param column_type: str
                列类型(默认为VARCHAR(100))
    
        return: None
        '''
        
        self.connect_db(database)#连接数据库
        cursor = self.conn.cursor()#创建游标
        cursor.execute("""
            ALTER TABLE %s ADD %s %s
            """%(table_name,column_name,column_type))#添加列
        self.conn.commit() # 提交
        self.close() # 关闭连接
        
    def delect_column(self,database,table_name,column_name):
        '''
        删除列
        
        param database: str
                数据库名
        param table_name: str
                表名
        param column_name: str
                列名
        return: None
        '''
        self.connect_db(database)
        cursor = self.conn.cursor()     
        cursor.execute("""
            ALTER TABLE %s DROP COLUMN %s
            """%(table_name,column_name))
        self.conn.commit()
        self.close() # 关闭连接 
        
        
        
    def insert_data(self,database,table_name,data): #添加数据(一次添加,适用于空表)
        '''
        添加数据(一次添加,适用于空表)
        
        param database: str
                数据库名
        param table_name: str
                表名
        param data: DataFrame
                数据
        return: None

        '''
        
        self.connect_db(database)
        cursor = self.conn.cursor() 
        sql3=''
        for d in range(len(data)):
            sql = '('
            for i in data.iloc[d,:]:
                sql += "'" + str(i) + "'" + ','
            sql2 = sql.strip(",")
            sql3 += sql2.strip()+'),'

            # 1000行执行一次sql
            if d%1000==0:
                sql3 = sql3.rstrip(",")
                sql1 = "INSERT INTO %s VALUES %s " % (table_name,sql3)
                # 执行sql语句
                sql1=sql1.replace("''","'")
                cursor.execute(sql1)
                sql = ""
                sql3=""
        try:
            sql3 = sql3.rstrip(",")
            sql1 = "INSERT INTO %s VALUES %s " % (table_name,sql3)
            sql1=sql1.replace("''","'")
            cursor.execute(sql1)      
        except:
            pass
        self.conn.commit() # 提交变更
        self.close() # 关闭连接
    
    def add_line(self,database,table_name,data): #添加多行数据(循环添加，一次添加一行,如果有重复数据，会报错,适用于有数据的表)
        '''
        添加多行数据(循环添加，一次添加一行,如果有重复数据，会报错,适用于有数据的表)

        param database: str
                数据库名
        param table_name: str
                表名    
        param data: DataFrame
                数据
        '''
        
        
        self.connect_db(database)
        cursor = self.conn.cursor() # 创建游标

        sql3=''
        for d in range(len(data)):
            sql = '('
            for i in data.iloc[d,:]:
                sql += "'" + str(i) + "'" + ','
            sql2 = sql.strip(",")
            sql3 += sql2.strip()+'),'
            try:
                sql3 = sql3.rstrip(",")
                sql1 = "INSERT INTO %s VALUES %s " % (table_name,sql3)
                # 执行sql语句
                sql1=sql1.replace("''","'")
                cursor.execute(sql1)
                sql = ""
                sql3=""
                self.conn.commit()
            except pymssql.IntegrityError as e:
                print("Error:", e)
                self.conn.rollback()

        self.close()
    
    #查询数据
    def select_data(self,database,table_name):
        '''
        查询数据

        param database: str
                数据库名
        param table_name: str
                表名    
        return: DataFrame
                数据    
                               
        '''
        self.connect_db(database)
        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM %s"%table_name)
        rows = cursor.fetchall()

        df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])

        self.close()
        return df
    def rollback(self):
        '''
        回滚
        '''
        self.conn.rollback()
        self.close()
    def get_all_table(self,database):
        '''
        获取数据库中所有表名
        param database: str
                数据库名
        return: list
                所有表名
        '''
        self.connect_db(database)
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT name FROM sysobjects WHERE xtype='U' ORDER BY name
            """)
        rows = cursor.fetchall()
        self.close()
        return rows


# commit