from flask import Flask, request
from models import Product, FarmerProduct, Order,Customer, db
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "your secret key"

db.init_app(app)
migrate = Migrate(app, db)
api = Api(app)
CORS(app)

@app.route('/')
def home():
    return {"msg":"Hello World"}

class Products(Resource):
    def get(self):
        product = [product.to_dict() for product in Product.query.all()]
        return product, 200
    
class Customers(Resource):
    def get(self):
        customers = [customer.to_dict() for customer in Customer.query.all()]
        return customers, 200
    
    def post(self):
        data = request.get_json()
        try:
            
            new_customer = Customer(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                location=data.get('location'),
                email=data.get('email'),
                phone=data.get('phone')
            )
            db.session.add(new_customer)
            db.session.commit()
            return new_customer.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400
            
class CustomerById(Resource):
    def get(self, customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            return customer.to_dict(), 200
        else:
            return {'error': 'Customer not found'}, 404
        
    def patch(self, customer_id):  
        customer = Customer.query.get(customer_id)
        if not customer:
            return {'error': 'Customer not found'}, 404
        data = request.get_json()
        try:
            
            if 'first_name' in data:
                customer.first_name = data['first_name']
            if 'last_name' in data:
                customer.last_name = data['last_name']
            if 'location' in data:
                customer.location = data['location']
            if 'email' in data:
                customer.email = data['email']
            if 'phone' in data:
                customer.phone = data['phone']
            
            db.session.commit()
            return customer.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 400

api.add_resource(Products, '/products')
api.add_resource(Customers, '/customers')
api.add_resource(CustomerById, '/customers/<int:customer_id>')

if __name__ == "__main__":
    app.run(debug=True, port=5555)

