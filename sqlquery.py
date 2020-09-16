import sqlite3
from myfields import myfields

conn = sqlite3.connect('mydatabase.db')

c = conn.cursor()

def insert_record(rec):
    with conn:
        c.execute("INSERT INTO My_Table VALUES (:field1, :field2, :field3)", {'field1': rec.field1, 'field2': rec.field2, 'field3': rec.field3})

def get_all():
    c.execute("SELECT * FROM My_Table")
    return c.fetchall()

def get_record_by_id(id_num):
    c.execute("SELECT * FROM My_Table WHERE id=:id", {'id': id_num})
    return c.fetchall()

def update_date(id_num, dateval):
    with conn:
        c.execute("""UPDATE My_table SET filed3 = :dateval
                    WHERE id = :id_num""", {'id': id_num, 'dateval': dateval})

def count_rows():
    with conn:
        c.execute("SELECT COUNT(*) FROM My_Table")
        c.fetchall()

def remove_record(id_num):
    with conn:
        c.execute("DELETE from My_Table WHERE id = :id_num", {'id_num': id_num})

print(count_rows())
result = c.execute("SELECT * FROM My_Table")
#num_of_rows = result[0][0]
print(result)

all_records = get_all()
print(all_records)

recbyid = get_record_by_id(1)
print(recbyid)