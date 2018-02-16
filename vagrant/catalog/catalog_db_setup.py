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
    title = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'title': self.title,
            'category_id': self.id
        }


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key = True)
    email = Column(String(120), nullable = False)
    username = Column(String(80), nullable=False)
    picture = Column(String(250), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'user_id': self.id,
            'title': self.title,
            'username':self.username,
            'picture':self.picture
        }


class Item(Base):
    __tablename__ = 'item'
    title = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'name': self.name,
            'description': self.description,
            'item_id': self.id,
        }
# End table definitions


engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine);