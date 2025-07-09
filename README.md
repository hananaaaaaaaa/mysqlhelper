# mysqlhelper
Python MySQL 操作封装类
```python
from src.mysql_helper import MySqlHelper

with MySqlHelper(password='your_password') as db:
    db.execute("INSERT INTO students (name) VALUES ('测试')")
    print(db.query("SELECT * FROM students"))
```
