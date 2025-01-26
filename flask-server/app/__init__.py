from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models

"""from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import sys
import os
import json

app = Flask(__name__)
CORS(app)

base_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(base_dir, "portfolio_db.db3")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    client = Client.add_user(data)
    if client and client.password == data.get("password"):
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid username or password"}), 400

@app.route("/create-account", methods=["POST"])
def create_account():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if get_client(username):
        return jsonify({"message": "Username already exists"}), 400
    
    new_client = create_client(username, password)

    return jsonify({"message": "Account created successfully"}), 201

@app.route("/stocks")
def displayStocks():
    file_path = os.path.join("data", "stocks.json")
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":
    if len(sys.argv) > 1:
        populate_db(sys.argv[1])

    app.run(debug=True)
"""
