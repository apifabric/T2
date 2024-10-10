# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  October 10, 2024 00:27:19
# Database: sqlite:////tmp/tmp.TVkX9oXBP7/Customer_API_iter_1/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX
from flask_login import UserMixin
import safrs, flask_sqlalchemy
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *



class Customer(SAFRSBaseX, Base):
    """
    description: Table to store basic customer demographic and contact information.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    AddressList : Mapped[List["Address"]] = relationship(back_populates="customer")
    CustomerInsightList : Mapped[List["CustomerInsight"]] = relationship(back_populates="customer")
    LoyaltyProgramList : Mapped[List["LoyaltyProgram"]] = relationship(back_populates="customer")
    OrderList : Mapped[List["Order"]] = relationship(back_populates="customer")



class Address(SAFRSBaseX, Base):
    """
    description: Table to store customer shipping and contact addresses.
    """
    __tablename__ = 'addresses'
    _s_collection_name = 'Address'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    address_line1 = Column(String, nullable=False)
    address_line2 = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("AddressList"))

    # child relationships (access children)



class CustomerInsight(SAFRSBaseX, Base):
    """
    description: Table to store aggregated insights about a customer.
    """
    __tablename__ = 'customer_insights'
    _s_collection_name = 'CustomerInsight'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    average_order_total = Column(Float)
    favorite_store = Column(String)
    last_purchase_date = Column(DateTime)
    most_purchased_category = Column(String)
    total_orders = Column(Integer)
    lifetime_value = Column(Float)
    order_frequency = Column(Float)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("CustomerInsightList"))

    # child relationships (access children)



class LoyaltyProgram(SAFRSBaseX, Base):
    """
    description: Table to store customer's loyalty program information.
    """
    __tablename__ = 'loyalty_programs'
    _s_collection_name = 'LoyaltyProgram'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    start_date = Column(DateTime)
    points_earned = Column(Integer, nullable=False)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("LoyaltyProgramList"))

    # child relationships (access children)



class Order(SAFRSBaseX, Base):
    """
    description: Table to store order history with insights about the customer.
    """
    __tablename__ = 'orders'
    _s_collection_name = 'Order'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    customer_id = Column(ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime)
    total_amount = Column(Float, nullable=False)
    store = Column(String)

    # parent relationships (access parent)
    customer : Mapped["Customer"] = relationship(back_populates=("OrderList"))

    # child relationships (access children)
    OrderItemList : Mapped[List["OrderItem"]] = relationship(back_populates="order")



class OrderItem(SAFRSBaseX, Base):
    """
    description: Table to store items for each order.
    """
    __tablename__ = 'order_items'
    _s_collection_name = 'OrderItem'  # type: ignore
    __bind_key__ = 'None'

    id = Column(Integer, primary_key=True)
    order_id = Column(ForeignKey('orders.id'), nullable=False)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price_per_unit = Column(Float, nullable=False)

    # parent relationships (access parent)
    order : Mapped["Order"] = relationship(back_populates=("OrderItemList"))

    # child relationships (access children)
