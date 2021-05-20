from peewee import *

import datetime

db = SqliteDatabase('db/database.db')
db.connect()

db.close()
