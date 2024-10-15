from flask import Flask
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
    
class
api.add_resource(Products, '/products')

if __name__ == "__main__":
    app.run(debug=True, port=5555)

