from app import app, db

class Tax(db.Model):
    __tablename__ = "tax"

    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, primary_key=False)
    province_state_id = db.Column(db.Integer, primary_key=False)
    capital_gain_tax = db.Column(db.Integer, primary_key=False)
    investment_income_tax = db.Column(db.Integer, primary_key=False)
    capital_gain_tax_credit = db.Column(db.Integer, primary_key=False) 
    eligible_dividend_tax_grossup = db.Column(db.Integer, primary_key=False)
    eligible_dividend_tax_credit = db.Column(db.Integer, primary_key=False)
    none_eligible_dividend_tax_grossup = db.Column(db.Integer, primary_key=False)
    none_eligible_dividend_tax_credit = db.Column(db.Integer, primary_key=False)

class Country(db.Model):
    __tablename__ = "country"

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(2), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    currency_id = db.Column(db.Integer, nullable=False)

class Stock(db.Model):
    __tablename__ = "stock"

    id = db.Column(db.Integer, primary_key = True)
    symbol = db.Column(db.String(20), nullable = False)
    name = db.Column(db.String(100), nullable = False)
    currency_id = db.Column(db.Integer, nullable = False)
    industry_id = db.Column(db.Integer, nullable = False)
    current_price = db.Column(db.Integer, nullable = False)
    expected_price = db.Column(db.Integer, nullable = False)
    eligible_divident = db.Column(db.Integer, nullable = False)
    none_eligible_divident = db.Column(db.Integer, nullable = False)
            

class Currency(db.Model):
    __tablename__ = "currency"

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(3), nullable = False)
    name = db.Column(db.String(100), nullable = False)

class Industry(db.Model):
    __tablename__ = "industry"

    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(3), nullable = False)
    name = db.Column(db.String(100), nullable = False)

class Portfolio(db.Model):
    __tablename__ = "portfolio"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    country_id = db.Column(db.Integer, nullable=False)
    province_state_id = db.Column(db.Integer, nullable=True)
    currency_id = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    is_small_company = db.Column(db.Integer, nullable=False)
    client_id = db.Column(db.Integer, nullable=False)

class PortfolioStock(db.Model):
    __tablename__ = "portfolio_stock"

    id = db.Column(db.Integer, primary_key= True)
    portfolio_id = db.Column(db.Integer, nullable=False)
    stock_id = db.Column(db.Integer, nullable=False)
    min_allocation = db.Column(db.Integer, nullable=False)
    max_allocation = db.Column(db.Integer, nullable=False)    

class Client(db.Model):
    __tablename__ = "client"

    id = db.Column(db.Integer, primary_key= True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    @classmethod
    def create_client(self, json_client):
        with app.app_context():
            client = create_client_from_json(json_client)
            db.session.add(client)
            db.session.commit()
    
    @classmethod
    def find_client(self, user_name):
        with app.app_context():
            client = db.session.query(Client).filter_by(user_name = user_name).first()
            return client

def create_client_from_json(json_client):
    return Client(
        first_name = json_client.get("first_name"),
        last_name = json_client.get("last_name"),
        user_name = json_client.get("username"),
        password = json_client.get("password")
    )
