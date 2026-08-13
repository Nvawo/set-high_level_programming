#!/usr/bin/python3
"""Defines a class to create a State."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Represents a state."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state"
    )
