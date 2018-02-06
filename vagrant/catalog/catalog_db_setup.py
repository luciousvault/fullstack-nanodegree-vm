#!/usr/bin/env python3
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Start table definitions
class Category(Base):
    __tablename__ = 'category'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)


class Item(Base):
    __tablename__ = 'item'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
# End table definitions


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine);