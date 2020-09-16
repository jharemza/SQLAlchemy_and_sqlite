import csv
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, Text, MetaData
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from myfields import myfields 

def Load_Data(file_name):
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        data = [tuple(row) for row in reader]
    # data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    print(data)
    print(data[0])
    print(data[0][0])
    # return data.tolist()
    return data

if __name__ == "__main__":
    t = time()

    engine = create_engine('sqlite:///mydatabase.db')
    Base.metadata.create_all(engine, checkfirst=True)
    
    Session = sessionmaker(bind=engine)
    s = Session()

    try:
        file_name = "mydata.csv"
        data = Load_Data(file_name)

        for i in data:
            record = myfields(**{
                'field1' : float(i[0]),
                'field2' : i[1],
                'field3' : datetime.strptime(i[2], '%m/%d/%Y')
                })
            print(record)
            s.add(record)
        
        s.commit()
    except:
        s.rollback()
        print('rollback executed')
    else:
        print('nothing went wrong')
    finally:
        s.close()
    print("Time elapsed: " + str(time() - t) + " s.")
