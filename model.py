from enum import unique
from peewee import *

db = SqliteDatabase('db/database.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    class Meta:
        database = db
        order_by='id'
        db_table='cats'

class Cat(BaseModel):
    name=CharField()

    class Meta:
        db_table='cats'

class Article(BaseModel):
    name=CharField()
    cat_id=ForeignKeyField(Cat)

    class Meta:
        db_table='articles'