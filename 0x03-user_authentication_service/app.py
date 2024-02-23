#!/usr/bin/env python3
""" doc doc doc """
from flask import Flask, jsonify, request, make_response, abort
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """doc doc doc"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        response = make_response(jsonify({"email": email, "message": "logged in"}), 200)
        response.set_cookie("session_id", AUTH.create_session(email))
        return response

    abort(401)


@app.route("/users", methods=["POST"])
def users():
    """doc doc doc"""
    email = request.form["email"]
    password = request.form["password"]
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/", methods=["GET"])
def welcome():
    """doc doc doc"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
