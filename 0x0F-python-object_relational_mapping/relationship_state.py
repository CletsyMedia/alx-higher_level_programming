#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_city import Base


class State(Base):
    """ The state class, contains state ID and name """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan")
