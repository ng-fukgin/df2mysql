请提供**df2mysql**的连接
**df2mysql** 是一个用于连接和操作 Microsoft SQL Server 数据库的 Python 包。它提供了一个名为 **Database** 的类，可以使用该类的方法执行各种数据库操作，如创建和删除数据库、创建和删除表、插入和检索数据等。

使用方法：
以下是使用 **df2mysql** 包的一般步骤：

1. 安装包：通过运行 **pip install df2mysql** 安装包。

2. 导入包：在你的 Python 脚本或交互式会话中使用 **from df2mysql import Database** 导入 **Database**类。

3.创建 **Database** 实例：通过创建 **Database** 类的实例并提供 SQL Server 主机、用户名和密码来建立数据库连接。

```python
db = Database(host='your_host', user='your_username', password='your_password')
```
4.连接到数据库：使用 **connect_db(database)** 方法连接到指定的数据库。


```python
db.connect_db(database='your_database')
```
5.执行数据库操作：使用 **Database** 类提供的方法执行数据库操作，如创建表、插入数据、检索数据等。


```python
db.create_table(database='your_database', table_name='your_table', table_head=['column1', 'column2'])
db.insert_data(database='your_database', table_name='your_table', data=your_data)
result = db.select_data(database='your_database', table_name='your_table')
```
6.关闭连接：在完成所有数据库操作后，使用 close() 方法关闭数据库连接。

```python
db.close()
```

请确保已安装 pymssql 和其他所需的依赖项，并提供正确的数据库连接信息。这样，你就可以使用 df2mysql 包连接到 Microsoft SQL Server 数据库并执行相应的操作了。
