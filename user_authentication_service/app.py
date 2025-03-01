#!/usr/bin/env python3
"""
Basic Flask app
"""

from flask import Flask, request, jsonify, abort, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def welcome():
    """
    Simple GET route that returns a welcome message.
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route("/users", methods=["POST"])
def register_user():
    """
    Endpoint to register a new user.

    Expected form data:
    - email (str): The user's email
    - password (str): The user's password

    Returns:
        JSON response with a success or error message.
    """
    # Récupération des données du formulaire
    email = request.form.get("email")
    password = request.form.get("password")

    # Vérification si les champs sont bien fournis
    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400

    try:
        # Tentative d'enregistrement du nouvel utilisateur
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        # Gestion du cas où l'utilisateur existe déjà
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    """
    email = request.form['email']
    password = request.form['password']

    if not email or not password:
        return jsonify({"message": "email and password are required"}), 400

    try:
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({
                "email": email,
                "message": "logged in"
            })
            response.set_cookie('session_id', session_id)
            return response, 200
        else:
            abort(401)
    except ValueError as e:
        abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> str:
    """Logout method to destroy a session"""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)

    try:
        user = AUTH.get_user_from_session_id(session_id)
        if not user:
            raise ValueError("User not found")
        AUTH.destroy_session(user.id)
        return redirect('/'), 302
    except ValueError:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile() -> str:
    """Profile method to get the user profile"""
    session_id = request.cookies.get('session_id')

    if not session_id:
        abort(403)

    try:
        user = AUTH.get_user_from_session_id(session_id)
        if not user:
            raise ValueError("User not found")
        return jsonify({"email": user.email}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """Get reset password token method to generate a token for resetting
        the password
    """
    email = request.form['email']

    if not email:
        return jsonify({"message": "email is required"}), 400

    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({
            "email": email,
            "reset_token": reset_token
        }), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """Update password method"""
    email = request.form['email']
    reset_token = request.form['reset_token']
    new_password = request.form['new_password']

    if not email or not reset_token or not new_password:
        return jsonify({
            "message": "email, reset_token and new_password are required"
        }), 400

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403, description="Invalid reset token")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
