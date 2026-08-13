#!/usr/bin/python3
"""Defines the State model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class State(Base):
    """Represent a state."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", back_populates="state")
