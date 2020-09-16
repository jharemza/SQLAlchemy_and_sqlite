import csv
from sqlalchemy import create_engine, Table, Column, Date, Text, Float, MetaData

engine = create_engine('sqlite:///sqlalchemy.db', echo=True)
 
metadata = MetaData()
# Define the table with sqlalchemy:
my_table = Table('MyTable', metadata,
    Column('field1', Float),
    Column('field2', Text),
    Column('field3', Date)
)
metadata.create_all(bind=engine)
insert_query = my_table.insert()

# Or read the definition from the DB:
# metadata.reflect(engine, only=['MyTable'])
# my_table = Table('MyTable', metadata, autoload=True, autoload_with=engine)
# insert_query = my_table.insert()

# Or hardcode the SQL query:
# insert_query = "INSERT INTO MyTable (foo, bar) VALUES (:foo, :bar)"

with open('mydata.csv', 'r', encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    engine.execute(
        insert_query,
        [{"field1": row[0], "field2": row[1], "field3": row[2]} 
            for row in csv_reader]
    )