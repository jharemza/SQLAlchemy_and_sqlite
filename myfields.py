from sqlalchemy import Column, Integer, Float, Date, Text
from base import Base

class myfields(Base):
    __tablename__ = 'My_Table'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, nullable=False)
    field1 = Column(Float)
    field2 = Column(Text)
    field3 = Column(Date)

    def __init__(self, field1, field2, field3):
        self.field1 = field1
        self.field2 = field2
        self.field3 = field3

    def __repr__(self):
        return "myfields('{}', '{}', '{}')".format(self.field1, self.field2, self.field3)