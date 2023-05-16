import sqlite3
import hashlib
#insert into Products values (?,'курица',500,1)
# insert into Products values (?,'яблоки',100,2)
# insert into Products values (?,'помидоры',150,3)
# insert into Products values (?,'черный хлеб',50,5)
# cat=int(input('введите категорию:'))
shpass=hashlib.sha256(b'pavel123')
data=('pavel',str(shpass.hexdigest()))
conn=sqlite3.connect('lesson10/products.db')
cur=conn.cursor()
cur.execute("""insert into Users(login,password) values(?,?)""",data)
conn.commit()
conn.close()
