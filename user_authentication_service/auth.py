#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password string using bcrypt and return the salted hash"""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Generate a string representation of a new UUID."""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user if the email does not exist,
            else raise ValueError.
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate the authentification of email and password provided
        """
        try:
            user = self._db.find_user_by(email=email)
            stored_hashed_password = user.hashed_password

            # Check if the provided password matches the stored hashed password
            if bcrypt.checkpw(password.encode('utf-8'),
                              stored_hashed_password):
                return True
            else:
                return False

        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session ID for the user corresponding to the given email.
        Returns:
            str: The generated session ID.
        """
        try:
            user = self._db.find_user_by(email=email)

            session_id = str(uuid.uuid4())

            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Return the user associated with the given session_id, or None"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy the session for the user by setting their session_id to None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            pass

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for the user"""
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError(f"User with email {email} does not exist")

    def update_password(self, reset_token: str, password: str) -> None:
        """Update the password for the user identified by the reset_token"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(
                user.id, hashed_password=hashed_password, reset_token=None)
        except NoResultFound:
            raise ValueError("Invalid reset token")
