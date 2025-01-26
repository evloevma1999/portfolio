from app import app
from app.models import Client, Stock, Tax, Country, Portfolio
from flask import render_template, request, jsonify, abort

import os
import json

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    client = Client.find_client(data.get("username"))
    if client and client.password == data.get("password"):
        return jsonify({"message": "Login successful", "client_id": client.id}), 200
    return jsonify({"error": "Invalid username or password"}), 400

@app.route("/create-account", methods=["POST"])
def create_account():
    data = request.json

    if Client.find_client(data.get("username")):
        return jsonify({"message": "Username already exists"}), 400
    
    Client.create_client(data)

    return jsonify({"message": "Account created successfully"}), 201

@app.route("/stocks", methods=["GET"])
def getAllStocks():
    stocks = Stock.query.all()
    stock_list = [
        {"id": stock.id, "symbol": stock.symbol, "name": stock.name, "currency_id": stock.currency_id,
         "industry_id": stock.industry_id, "current_price": stock.current_price, "expected_price": stock.expected_price,
         "eligible_divident": stock.eligible_divident, "none_eligible_divident": stock.none_eligible_divident}
        for stock in stocks
    ]
    return jsonify(stock_list)


@app.route("/taxes", methods=["GET"])
def getAllTaxes():
    taxes = Tax.query.all()
    tax_list = [
        {"id": tax.id, "country_id": tax.country_id, "province_state_id": tax.province_state_id,
         "capital_gain_tax": tax.capital_gain_tax, "investment_income_tax": tax.investment_income_tax,
         "capital_gain_tax_credit": tax.capital_gain_tax_credit, "eligible_dividend_tax_grossup": tax.eligible_dividend_tax_grossup,
         "eligible_dividend_tax_credit": tax.eligible_dividend_tax_credit, "none_eligible_dividend_tax_grossup": tax.none_eligible_dividend_tax_grossup,
         "none_eligible_dividend_tax_credit": tax.none_eligible_dividend_tax_credit}
        for tax in taxes
    ]
    return jsonify(tax_list)

@app.route("/countries", methods=["GET"])
def getAllCountries():
    countries = Country.query.all()
    country_list = [
            {"id": country.id, "code": country.code, "name": country.name, "currency_id": country.currency_id}
            for country in countries
    ]
    return jsonify(country_list)

@app.route("/api/portfolios/<int:client_id>", methods=["GET"])
def getClientPortfolios(client_id):
        portfolios = Portfolio.query.filter_by(client_id=client_id)
        serialized_portfolios = [
             {
                "id": portfolio.id,
                "name": portfolio.name,
                "description": portfolio.description,
                "country": portfolio.country_id,
                "currency": portfolio.currency_id,
                "balance": portfolio.balance
            }
             for portfolio in portfolios
        ]
        return jsonify(serialized_portfolios), 200


@app.route("/portfolio/<string:portfolio_name>", methods=["GET"])
def getPortfolio(portfolio_name):
        portfolio = Portfolio.query.filter_by(name=portfolio_name).first()

        if not portfolio:
            abort(404, description="Portfolio not found")

        serialized_portfolio = {
            "id": portfolio.id,
            "name": portfolio.name,
            "description": portfolio.description,
            "country": portfolio.country_id,
            "currency": portfolio.currency_id,
            "balance": portfolio.balance
        }

        # Return the serialized portfolio
        return jsonify(serialized_portfolio), 200