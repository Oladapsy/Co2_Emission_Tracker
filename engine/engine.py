#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy import Column, Float, Integer, String 
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://oladapsy:1234@localhost/co2db", encoding='latin1', echo=True)
Base = declarative_base()

class Co2record(Base):
    """ the Co2 record table which is a class"""
    __tablename__ = 'Co2record'

    id = Column(Integer, primary_key=True)
    date = Column(String(20))
    cycle = Column(Float(8))
    trend = Column(Float(8))


    def __repr__(self):
        """ the instance representation"""
        return f"Record (date={self.date} cycle={self.cycle} trend={self.trend})"
