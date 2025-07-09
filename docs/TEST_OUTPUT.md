huangxianuo@MacBook-Air-77 ~ % mysql_secure_installation

Securing the MySQL server deployment.

Enter password for user root: 
Error: Access denied for user 'root'@'localhost' (using password: YES)
huangxianuo@MacBook-Air-77 ~ % *mysql_secure_installation
zsh: no matches found: *mysql_secure_installation
huangxianuo@MacBook-Air-77 ~ % mysql_secure_installation

Securing the MySQL server deployment.

Enter password for user root: 
Error: Access denied for user 'root'@'localhost' (using password: NO)
huangxianuo@MacBook-Air-77 ~ % mysql_secure_installation

Securing the MySQL server deployment.

Enter password for user root: 

VALIDATE PASSWORD COMPONENT can be used to test passwords
and improve security. It checks the strength of password
and allows the users to set only those passwords which are
secure enough. Would you like to setup VALIDATE PASSWORD component?

Press y|Y for Yes, any other key for No: y

There are three levels of password validation policy:

LOW    Length >= 8
MEDIUM Length >= 8, numeric, mixed case, and special characters
STRONG Length >= 8, numeric, mixed case, special characters and dictionary                  file

Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 1
Using existing password for root.

Estimated strength of the password: 50 
Change the password for root ? ((Press y|Y for Yes, any other key for No) : y

New password: 

Re-enter new password: 

Estimated strength of the password: 50 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
 ... Failed! Error: Your password does not satisfy the current policy requirements

New password: 

Re-enter new password: 

Estimated strength of the password: 100 
Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
By default, a MySQL installation has an anonymous user,
allowing anyone to log into MySQL without having to have
a user account created for them. This is intended only for
testing, and to make the installation go a bit smoother.
You should remove them before moving into a production
environment.

Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
Success.


Normally, root should only be allowed to connect from
'localhost'. This ensures that someone cannot guess at
the root password from the network.

Disallow root login remotely? (Press y|Y for Yes, any other key for No) : No

 ... skipping.
By default, MySQL comes with a database named 'test' that
anyone can access. This is also intended only for testing,
and should be removed before moving into a production
environment.


Remove test database and access to it? (Press y|Y for Yes, any other key for No) : y
 - Dropping test database...
Success.

 - Removing privileges on test database...
Success.

Reloading the privilege tables will ensure that all changes
made so far will take effect immediately.

Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
Success.

All done! 
huangxianuo@MacBook-Air-77 ~ % mysql -u root -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 15
Server version: 9.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE IF NOT EXISTS school;
Query OK, 1 row affected (0.103 sec)

mysql> USE school;CREATE TABLE students (
Database changed
    ->     student_id INT PRIMARY KEY AUTO_INCREMENT,
    ->     name VARCHAR(50) NOT NULL,
    ->     height DECIMAL(5,2) COMMENT '单位：厘米'
    -> ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
Query OK, 0 rows affected (0.041 sec)

mysql> Query OK, 0 rows affected (0.004 sec)

mysql> INSERT INTO students (name, height) VALUES ('张三', 175.5);
Query OK, 1 row affected (0.028 sec)

mysql> 
mysql> Query OK, 0 rows affected (0.000 sec)

mysql> INSERT INTO students (name, height) VALUES 
    -> ('李四', 168.0),
    -> ('王五', 182.3),
    -> ('赵六', 170.7);
Query OK, 3 rows affected (0.004 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> SELECT * FROM students;
+------------+--------+--------+
| student_id | name   | height |
+------------+--------+--------+
|          1 | 张三   | 175.50 |
|          2 | 李四   | 168.00 |
|          3 | 王五   | 182.30 |
|          4 | 赵六   | 170.70 |
+------------+--------+--------+
4 rows in set (0.005 sec)

mysql> SELECT * FROM students WHERE height > 170;
+------------+--------+--------+
| student_id | name   | height |
+------------+--------+--------+
|          1 | 张三   | 175.50 |
|          3 | 王五   | 182.30 |
|          4 | 赵六   | 170.70 |
+------------+--------+--------+
3 rows in set (0.076 sec)

mysql> UPDATE students SET height = 176.0 WHERE name = '张三';
Query OK, 1 row affected (0.038 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> DELETE FROM students WHERE name = '赵六';
Query OK, 1 row affected (0.007 sec)

mysql> SELECT student_id AS 学号, name AS 姓名, height AS 身高 
    -> FROM students 
    -> ORDER BY height DESC;
+--------+--------+--------+
| 学号   | 姓名   | 身高   |
+--------+--------+--------+
|      3 | 王五   | 182.30 |
|      1 | 张三   | 176.00 |
|      2 | 李四   | 168.00 |
+--------+--------+--------+
3 rows in set (0.009 sec)

mysql> 
mysql> 

huangxianuo@MacBook-Air-77 ~ % brew install python
==> Downloading https://formulae.brew.sh/api/formula.jws.json
==> Downloading https://formulae.brew.sh/api/cask.jws.json
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.13/manifests/3.13.5-1
######################################################################### 100.0%
==> Fetching dependencies for python@3.13: mpdecimal, readline, sqlite and expat
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/4.0.1
######################################################################### 100.0%
==> Fetching mpdecimal
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/blobs/sha256:51a9fd90
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.3
######################################################################### 100.0%
==> Fetching readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/blobs/sha256:875c8524e
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.50.2
######################################################################### 100.0%
==> Fetching sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/blobs/sha256:198026e2cf3
######################################################################### 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/expat/manifests/2.7.1
######################################################################### 100.0%
==> Fetching expat
==> Downloading https://ghcr.io/v2/homebrew/core/expat/blobs/sha256:4e9eb804bd04
######################################################################### 100.0%
==> Fetching python@3.13
==> Downloading https://ghcr.io/v2/homebrew/core/python/3.13/blobs/sha256:c879de
######################################################################### 100.0%
==> Installing dependencies for python@3.13: mpdecimal, readline, sqlite and expat
==> Installing python@3.13 dependency: mpdecimal
==> Downloading https://ghcr.io/v2/homebrew/core/mpdecimal/manifests/4.0.1
Already downloaded: /Users/huangxianuo/Library/Caches/Homebrew/downloads/dbbf60721dc54b6215f6c0988496331d4110a2a358da867a1129cd84b8166b31--mpdecimal-4.0.1.bottle_manifest.json
==> Pouring mpdecimal--4.0.1.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/mpdecimal/4.0.1: 22 files, 641.7KB
==> Installing python@3.13 dependency: readline
==> Downloading https://ghcr.io/v2/homebrew/core/readline/manifests/8.3
Already downloaded: /Users/huangxianuo/Library/Caches/Homebrew/downloads/cb2894c34ae3c9e9118c0e51ad0bacfd66f85aca21cc933254a4b084a869712a--readline-8.3.bottle_manifest.json
==> Pouring readline--8.3.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/readline/8.3: 56 files, 2.6MB
==> Installing python@3.13 dependency: sqlite
==> Downloading https://ghcr.io/v2/homebrew/core/sqlite/manifests/3.50.2
Already downloaded: /Users/huangxianuo/Library/Caches/Homebrew/downloads/174a21a1715a51dca20bbf72e02d1f2f53cf5faa29f2301178aa70bdde5a5cb0--sqlite-3.50.2.bottle_manifest.json
==> Pouring sqlite--3.50.2.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/sqlite/3.50.2: 13 files, 4.9MB
==> Installing python@3.13 dependency: expat
==> Downloading https://ghcr.io/v2/homebrew/core/expat/manifests/2.7.1
Already downloaded: /Users/huangxianuo/Library/Caches/Homebrew/downloads/09efb27f4cd66decc2e0f393e7f9292c729064e5c939cd8191f81fc000c3947a--expat-2.7.1.bottle_manifest.json
==> Pouring expat--2.7.1.arm64_sonoma.bottle.tar.gz
🍺  /opt/homebrew/Cellar/expat/2.7.1: 23 files, 684.4KB
==> Installing python@3.13
==> Pouring python@3.13--3.13.5.arm64_sonoma.bottle.1.tar.gz
==> Caveats
Python is installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, are installed into
  /opt/homebrew/opt/python@3.13/libexec/bin

See: https://docs.brew.sh/Homebrew-and-Python
==> Summary
🍺  /opt/homebrew/Cellar/python@3.13/3.13.5: 3,605 files, 66.9MB
==> Running `brew cleanup python@3.13`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
==> Caveats
==> python@3.13
Python is installed as
  /opt/homebrew/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, are installed into
  /opt/homebrew/opt/python@3.13/libexec/bin

See: https://docs.brew.sh/Homebrew-and-Python
huangxianuo@MacBook-Air-77 ~ % python3 --version
pip3 --version
Python 3.13.5
pip 25.1.1 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)
huangxianuo@MacBook-Air-77 ~ % pip install pymysql
zsh: command not found: pip
huangxianuo@MacBook-Air-77 ~ % pip3 --version
pip 25.1.1 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)
huangxianuo@MacBook-Air-77 ~ % python -m pip --version
zsh: command not found: python
huangxianuo@MacBook-Air-77 ~ % curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 2225k  100 2225k    0     0  1905k      0  0:00:01  0:00:01 --:--:-- 1913k
huangxianuo@MacBook-Air-77 ~ % python get-pip.py
zsh: command not found: python
huangxianuo@MacBook-Air-77 ~ % brew install python
Warning: python@3.13 3.13.5 is already installed and up-to-date.
To reinstall 3.13.5, run:
  brew reinstall python@3.13
huangxianuo@MacBook-Air-77 ~ % echo "alias python=python3" >> ~/.zshrc
echo "alias pip=pip3" >> ~/.zshrc
source ~/.zshrc
huangxianuo@MacBook-Air-77 ~ % pip install pymysql
Collecting pymysql
  Downloading PyMySQL-1.1.1-py3-none-any.whl.metadata (4.4 kB)
Downloading PyMySQL-1.1.1-py3-none-any.whl (44 kB)
Installing collected packages: pymysql
Successfully installed pymysql-1.1.1
huangxianuo@MacBook-Air-77 ~ % python -c "import pymysql; print(pymysql.__version__)"
1.4.6
huangxianuo@MacBook-Air-77 ~ % mysql -u root -p -e "SHOW DATABASES;"
Enter password: 
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| school             |
| sys                |
+--------------------+
huangxianuo@MacBook-Air-77 ~ % python3 mysqlhelper.py 
huangxianuo@MacBook-Air-77 ~ % python3 mysqlhelper.py

  File "/Users/huangxianuo/mysqlhelper.py", line 50
    for s in db.query("SELECT student_id AS id, name, height FROM students"):
IndentationError: unexpected indent
huangxianuo@MacBook-Air-77 ~ % python3 mysqlhelper.py
输入MySQL密码:
使用别名(student_id→id)
ID: 1, 姓名: 张三, 身高: 176.0cm
ID: 2, 姓名: 李四, 身高: 168.0cm
ID: 3, 姓名: 王五, 身高: 182.3cm
huangxianuo@MacBook-Air-77 ~ % python3 mysqlhelper.py > output.txt 2>&1
