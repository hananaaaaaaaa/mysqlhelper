import pymysql

class MySqlHelper:
    def __init__(self, host='localhost', user='root', password='', database='school'):
 
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )
    
    def execute(self, sql, params=()):
       
        with self.conn.cursor() as c:
            c.execute(sql, params)
            self.conn.commit()
            return c.rowcount
    
    def query(self, sql, params=()):
        
        with self.conn.cursor() as c:
            c.execute(sql, params)
            return c.fetchall()
    
    def close(self):
      
        self.conn.close()


if __name__ == '__main__':
    db = MySqlHelper(password=input("输入密码: "))
    print(db.query("SHOW TABLES"))  
    db.close()
