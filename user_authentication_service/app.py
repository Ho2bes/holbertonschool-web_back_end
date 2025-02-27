#!/usr/bin/env python3
"""
Basic Flask app with authentication
"""

from flask import Flask, request, jsonify, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome():
    """
    Simple GET route that returns a welcome message.
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """
    Register a new user.

    Expected form data:
    - email (str): User's email
    - password (str): User's password

    Returns:
        JSON response with success or error message.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "User created"}), 201
    except ValueError:
        return jsonify({"message": "Email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    Login user and create a session.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "Logged in"})
        response.set_cookie('session_id', session_id)
        return response, 200
    return abort(401, description="Invalid credentials")


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Logout user and destroy session.
    """
    session_id = request.cookies.get('session_id')

    if not session_id:
        return abort(403, description="Missing session ID")

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return abort(403, description="Invalid session")

    AUTH.destroy_session(user.id)
    return redirect('/'), 302


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    Retrieve user profile based on session.
    """
    session_id = request.cookies.get('session_id')

    if not session_id:
        return abort(403, description="Missing session ID")

    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        return abort(403, description="Invalid session")

    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    Generate reset password token.
    """
    email = request.form.get("email")

    if not email:
        return jsonify({"message": "Email is required"}), 400

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        return abort(403, description="Email not found")


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
    Update user password with reset token.
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    if not email or not reset_token or not new_password:
        return jsonify({"message": "Email, reset_token, and new_password are required"}), 400

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        return abort(403, description="Invalid reset token")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
