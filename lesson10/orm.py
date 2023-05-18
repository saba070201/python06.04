from peewee import *
conn=SqliteDatabase('test.db')

class User(Model):
    id=PrimaryKeyField(column_name='id')
    name=TextField(column_name='name')
    class Meta:
        table_name='users'
        database=conn

for i in User.select().where(User.name=='misha1'):
    print(i.name)
# comment