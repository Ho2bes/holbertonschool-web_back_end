#!/usr/bin/env python3

"""DB module
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import Optional

from user import Base, User


class DB:
    """DB class to manage database operations."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.create_all(self._engine)  # Ne supprime plus les données existantes
        self.__session: Optional[Session] = None

    @property
    def _session(self) -> Session:
        """Return a memoized session object."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): User's email.
            hashed_password (str): User's hashed password.

        Returns:
            User: The created user object.
        """
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
            return new_user
        except Exception as e:
            self._session.rollback()  # Annuler en cas d'erreur
            raise RuntimeError(f"Error while adding user: {e}")

    def find_user_by(self, **kwargs) -> User:
        """Find a user by arbitrary keyword arguments.

        Args:
            **kwargs: Arbitrary key-value pairs to filter the user.

        Returns:
            User: The matching user.

        Raises:
            NoResultFound: If no user matches the query.
            InvalidRequestError: If an invalid argument is provided.
        """
        session = self._session
        try:
            return session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise NoResultFound("No user found matching the given criteria.")
        except InvalidRequestError:
            raise InvalidRequestError("Invalid query parameters provided.")

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user attributes.

        Args:
            user_id (int): The ID of the user to update.
            **kwargs: The attributes to update.

        Raises:
            ValueError: If an attribute does not exist.
            RuntimeError: If an error occurs during commit.
        """
        session = self._session
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError(f"User object has no attribute '{key}'")
            setattr(user, key, value)

        try:
            session.commit()
        except Exception as e:
            session.rollback()  # Annuler en cas d'erreur
            raise RuntimeError(f"Error while updating user: {e}")
