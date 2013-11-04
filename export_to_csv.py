import csv
import sqlalchemy as sqAl

metadata = sqAl.MetaData()
engine = sqAl.create_engine('sqlite:///%s' % 'data.db')
metadata.bind = engine

mytable = sqAl.Table('sometable', metadata, autoload=True)
db_connection = engine.connect()

select = sqAl.sql.select([mytable])
result = db_connection.execute(select)

fh = open('data.csv', 'wb')
outcsv = csv.writer(fh)

outcsv.writerow(result.keys())
outcsv.writerows(result)

fh.close
