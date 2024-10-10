import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py



from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Create a database connection
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite', echo=True)

Base = declarative_base()

class Customer(Base):
    """description: Table to store basic customer demographic and contact information."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)

class Address(Base):
    """description: Table to store customer shipping and contact addresses."""
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)

class Order(Base):
    """description: Table to store order history with insights about the customer."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float, nullable=False)
    store = Column(String, nullable=True)

class CustomerInsights(Base):
    """description: Table to store aggregated insights about a customer."""
    __tablename__ = 'customer_insights'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    average_order_total = Column(Float, nullable=True)
    favorite_store = Column(String, nullable=True)
    last_purchase_date = Column(DateTime, nullable=True)
    most_purchased_category = Column(String, nullable=True)
    total_orders = Column(Integer, nullable=True)
    lifetime_value = Column(Float, nullable=True)
    order_frequency = Column(Float, nullable=True) # Days between orders

class LoyaltyProgram(Base):
    """description: Table to store customer's loyalty program information."""
    __tablename__ = 'loyalty_programs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    points_earned = Column(Integer, nullable=False)

class OrderItem(Base):
    """description: Table to store items for each order."""
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)

# Create all tables
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Insert sample data
customer1 = Customer(first_name='John', last_name='Doe', email='john.doe@example.com', phone_number='123-456-7890')
customer2 = Customer(first_name='Jane', last_name='Smith', email='jane.smith@example.com')

address1 = Address(customer_id=1, address_line1='123 Elm St', city='Springfield', state='IL', postal_code='62701', country='USA')
address2 = Address(customer_id=2, address_line1='456 Maple Ave', city='Shelbyville', state='IL', postal_code='62565', country='USA')

order1 = Order(customer_id=1, total_amount=150.75, store='Downtown')
order2 = Order(customer_id=2, total_amount=270.12, store='Mall')

insight1 = CustomerInsights(customer_id=1, average_order_total=150.75, favorite_store='Downtown', last_purchase_date=datetime.datetime(2023, 10, 15), most_purchased_category='Clothing', total_orders=1, lifetime_value=150.75, order_frequency=30.0)
insight2 = CustomerInsights(customer_id=2, average_order_total=270.12, favorite_store='Mall', last_purchase_date=datetime.datetime(2023, 10, 10), most_purchased_category='Electronics', total_orders=1, lifetime_value=270.12, order_frequency=15.0)

loyalty1 = LoyaltyProgram(customer_id=1, points_earned=500)
loyalty2 = LoyaltyProgram(customer_id=2, points_earned=200)

order_item1 = OrderItem(order_id=1, product_name='Socks', quantity=3, price_per_unit=5.99)
order_item2 = OrderItem(order_id=2, product_name='T-Shirt', quantity=2, price_per_unit=19.99)

# Add instances to session
session.add_all([
    customer1, customer2, address1, address2, order1, order2, 
    insight1, insight2, loyalty1, loyalty2, order_item1, order_item2
])

# Commit the transaction
session.commit()

# Close the session
session.close()
