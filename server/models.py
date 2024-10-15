from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Farmer(db.Model, SerializerMixin):
    __tablename__ = 'farmers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)

    farmer_products = db.relationship('FarmerProduct', back_populates='farmer')

    def __repr__(self):
        return f'<Farmer {self.first_name} {self.last_name}>'

class FarmerProduct(db.Model, SerializerMixin):
    __tablename__ = 'farmer_products'
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    farmer = db.relationship('Farmer', back_populates='farmer_products')
    product = db.relationship('Product', back_populates='farmer_products')

    serialize_rules = ('-farmer_products.farmer', '-farmer_products.product')

    def __repr__(self):
        return f'<FarmerProduct {self.farmer_id} {self.product_id}>'

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.String(120), nullable=False)
    product_image = db.Column(db.String(120), nullable=False)

    farmer_products = db.relationship('FarmerProduct', back_populates='product')
    orders = db.relationship('Order', back_populates='product')  

    serialize_only = ('id', 'product_name', 'description', 'price', 'quantity', 'product_image')

    def __repr__(self):
        return f'<Product {self.product_name}>'

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), unique=True, nullable=False)
    
    orders = db.relationship('Order', back_populates='customer')

    serialize_only = ('id', 'first_name', 'last_name', 'location', 'email', 'phone')

    def __repr__(self):
        return f'<Customer {self.first_name} {self.last_name}>'

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False) 
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)

    customer = db.relationship('Customer', back_populates='orders')
    product = db.relationship('Product', back_populates='orders') 

    serialize_only = ('id', 'quantity', 'product_id', 'customer_id')

    def __repr__(self):
        return f'<Order {self.id} Product {self.product_id}>'
