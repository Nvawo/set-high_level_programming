#!/usr/bin/python3
"""Defines the State class."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base


class State(Base):
    """Represents a state."""

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state"
    )
