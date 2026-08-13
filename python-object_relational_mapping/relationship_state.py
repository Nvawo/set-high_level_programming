#!/usr/bin/python3
"""State class definition for relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base
from relationship_city import City


class State(Base):
    """State representation."""

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column(String(128), nullable=False)

    cities = relationship(
        "City",
        cascade="all, delete, delete-orphan",
        backref="state"
    )
