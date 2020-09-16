import sqlite3
import csv
from myfields import myfields

conn = sqlite3.connect('mydatabase.db')

c = conn.cursor()

c.execute("""CREATE TABLE My_Table (
            id INTEGER PRIMARY KEY ASC,
            field1 REAL,
            field2 TEXT,
            field3 TEXT
            )""")


def insert_record(rec):
    with conn:
        c.execute("INSERT INTO My_Table VALUES (:field1, :field2, :field3)", {'field1': rec.field1, 'field2': rec.field2, 'field3': rec.field3})


def get_record_by_id(id_num):
    c.execute("SELECT * FROM My_Table WHERE id=:id", {'id': id_num})
    return c.fetchall()


def update_date(id_num, dateval):
    with conn:
        c.execute("""UPDATE My_table SET filed3 = :dateval
                    WHERE id = :id_num""", {'id': id_num, 'dateval': dateval})

def get_all():
    c.execute("SELECT * FROM My_Table")
    return c.fetchall()

def count_rows():
    with conn:
        c.execute("SELECT COUNT(*) FROM My_Table")
        c.fetchall()

def remove_record(id_num):
    with conn:
        c.execute("DELETE from My_Table WHERE id = :id_num", {'id_num': id_num})

def Load_Data(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        data = [tuple(row) for row in reader]
        return data

#emp_2 = Employee('Jane', 'Doe', 90000)
#emp_1 = Employee('John', 'Doe', 80000)
#
#insert_emp(emp_1)
#insert_emp(emp_2)
#
#emps = get_emps_by_name('Doe')
#print(emps)
#
#update_pay(emp_2, 95000)
#remove_emp(emp_1)
#
#emps = get_emps_by_name('Doe')
#print(emps)

def main():

    csv_file = 'mydata.csv'
    data = Load_Data(csv_file)

    for i in data:
            record = myfields(**{
                'field1' : i[0],
                'field2' : i[1],
                'field3' : i[2]
                })
            print(record)
            insert_record(record)

    print(count_rows())
    result = c.execute("SELECT * FROM My_Table")
    #num_of_rows = result[0][0]
    print(result)

    all_records = get_all()
    print(all_records)

    recbyid = get_record_by_id(1)
    print(recbyid)

    conn.close()

if __name__ == '__main__':
    main()