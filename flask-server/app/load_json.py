from models import Tax, Country, Stock, Currency, Industry, Portfolio, PortfolioStock
from app import db, app
from flask import abort

import json
import os


file_map = {'T': "taxes.json", 'S': "stocks.json", 'P': "portfolios.json"}

def populate_db(arg):
    """Loads json file into database based on command-line argument"""

    if arg not in file_map:
        print("command line argument is not valid")
        abort(400)
    
    file_name = file_map[arg]
    file_path = os.path.join("data", file_name)

    with open(file_path, 'r') as f:
        data = json.load(f)
    
    end_of_file_name = file_name.find('.')
    json_name = file_name[:end_of_file_name]

    insert_data(data.get(json_name), json_name)

def insert_data(data, json_name):
    map_json_to_db = select_create_function(json_name)
    with app.app_context():
        for entry in data:
            new_item = map_json_to_db(entry)
            db.session.add(new_item)
            try:
                db.session.commit()
                print("Data stored successfully!")
            except Exception as e:
                db.session.rollback()
                print(f"Error importing data: {e}")
            if json_name == "portfolios":
                store_portfolio_stocks(entry, new_item.id)

def store_portfolio_stocks(entry, portfolio_id):
    for portfolio_stock_json in entry.get("portfolio_stocks"):
        portfolio_stock_json["portfolio_id"] = portfolio_id
        portfolio_stock_db = create_portfolio_stock_db_object(portfolio_stock_json)
        db.session.add(portfolio_stock_db)
        try:
            db.session.commit()
            print("Data stored successfully!")
        except Exception as e:
            db.session.rollback()
            print(f"Error importing data: {e}")

def select_create_function(table_name):
    match table_name:
        case "taxes":
            return create_tax_db_object
        case "stocks":
            return create_stock_db_object
        case "portfolios":
            return create_portfolio_db_object
        case "portfolio_stock":
            return create_portfolio_stock_db_object

def create_portfolio_stock_db_object(entry):
    return PortfolioStock(
        portfolio_id = entry.get("portfolio_id"),
        stock_id = get_stock_id_from_symbol(entry.get("symbol")),
        min_allocation = entry.get("min_allocation"),
        max_allocation = entry.get("max_allocation")
    )

def create_portfolio_db_object(entry):
    return Portfolio(
        name = entry.get("name"),
        description = entry.get("description"),
        country_id = get_id_from_code(Country, entry.get("country_code")),
        province_state_id = entry.get("province_state_id"),
        currency_id = get_id_from_code(Currency, entry.get("currency_code")),
        balance = entry.get("balance"),
        is_small_company = entry.get("is_small_company")
    )

def create_stock_db_object(entry):
    return Stock(
        symbol = entry.get("symbol"),
        name = entry.get("name"),
        currency_id = get_id_from_code(Currency, entry.get("currency_code")),
        industry_id = get_id_from_code(Industry, entry.get("industry_code")),
        current_price = entry.get("current_price"),
        expected_price = entry.get("expected_price"),
        eligible_divident = entry.get("eligible_divident"),
        none_eligible_divident = entry.get("none_eligible_divident")
    )


def create_tax_db_object(entry):
    return Tax(
                country_id = get_id_from_code(Country, entry.get('country_code')), 
                province_state_id = entry.get('province_state_code'), 
                capital_gain_tax = entry.get('capital_gain_tax'), 
                investment_income_tax = entry.get('investment_income_tax'), 
                capital_gain_tax_credit = entry.get('capital_gain_tax_credit'), 
                eligible_dividend_tax_grossup = entry.get('eligible_dividend_tax_grossup'), 
                eligible_dividend_tax_credit = entry.get('eligible_dividend_tax_credit'), 
                none_eligible_dividend_tax_grossup = entry.get('none_eligible_dividend_tax_grossup'), 
                none_eligible_dividend_tax_credit = entry.get('none_eligible_dividend_tax_credit')
            )

def get_id_from_code(model_class, code):
    row = db.session.query(model_class).filter_by(code=code).first()

    if row:
        print(f"Found {model_class.name}: {row.name} (ID: {row.id})")
    else:
        print(f"No {model_class.name} found with code: {code}")
        abort(400)

    return row.id

def get_stock_id_from_symbol(stock_symbol):
    row = db.session.query(Stock).filter_by(symbol = stock_symbol).first()

    if row:
        print(f"Found Stock: {row.name} (ID: {row.id})")
    else:
        print(f"No row found with code: {stock_symbol}")
        abort(400)
    
    return row.id
