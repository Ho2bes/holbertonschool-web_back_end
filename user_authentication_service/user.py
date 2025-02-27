#!/usr/bin/env python3
"""
User model for SQLAlchemy.
Defines a user table with id, email, hashed_password, session_id, and reset_token.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()

MAX_STRING_LENGTH = 250  # Définition d'une constante pour les champs String


class User(Base):
    """
    User model representing a user in the database.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(MAX_STRING_LENGTH), nullable=False, unique=True)
    hashed_password = Column(String(MAX_STRING_LENGTH), nullable=False)
    session_id = Column(String(MAX_STRING_LENGTH), nullable=True)
    reset_token = Column(String(MAX_STRING_LENGTH), nullable=True)

    def __repr__(self) -> str:
        """
        String representation of a User instance.
        """
        return f"<User(id={self.id}, email={self.email})>"
