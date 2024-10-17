from flask import Flask, request
from models import Product, FarmerProduct, Order, User, db
from flask_restful import Api, Resource
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
    return {"msg": "Hello World"}

class Products(Resource):
    def get(self):
        products = [product.to_dict() for product in Product.query.all()]
        return products, 200

class Users(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200
    
    def post(self):
        data = request.get_json()
        try:
            new_user = User(
                first_name=data.get('first_name'),
                last_name=data.get('last_name'),
                location=data.get('location'),
                email=data.get('email'),
                phone=data.get('phone'),
                user_type=data.get('user_type')  # 'customer' or 'farmer'
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(), 201
        except Exception as e:
            return {'error': str(e)}, 400

class UserById(Resource):
    def get(self, user_id):
        user = User.query.get(user_id)
        if user:
            return user.to_dict(), 200
        else:
            return {'error': 'User not found'}, 404
        
    def patch(self, user_id):  
        user = User.query.get(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        data = request.get_json()
        try:
            if 'first_name' in data:
                user.first_name = data['first_name']
            if 'last_name' in data:
                user.last_name = data['last_name']
            if 'location' in data:
                user.location = data['location']
            if 'email' in data:
                user.email = data['email']
            if 'phone' in data:
                user.phone = data['phone']
            if 'user_type' in data:
                user.user_type = data['user_type']
            
            db.session.commit()
            return user.to_dict(), 200
        except Exception as e:
            return {'error': str(e)}, 400

api.add_resource(Products, '/products')
api.add_resource(Users, '/users')
api.add_resource(UserById, '/users/<int:user_id>')

if __name__ == "__main__":
    app.run(debug=True, port=5555)
