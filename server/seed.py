from app import app
from models import Product, FarmerProduct, Order, Customer, Farmer, db

with app.app_context():
    

    farmers = [
        Farmer(first_name='Alice', last_name='Smith', location='Farmville', email='alice@example.com', phone='+1-555-1234'),
        Farmer(first_name='Bob', last_name='Johnson', location='Countryside', email='bob@example.com', phone='+1-555-5678'),
        Farmer(first_name='Charlie', last_name='Williams', location='Riverside', email='charlie@example.com', phone='+1-555-9101'),
        Farmer(first_name='David', last_name='Jones', location='Hilltop', email='david@example.com', phone='+1-555-1122'),
        Farmer(first_name='Eva', last_name='Brown', location='Meadow', email='eva@example.com', phone='+1-555-3344'),
    ]


    products = [
        Product(product_name='Tomato', description='Fresh and organic', price='2.50', quantity='100', product_image='https://example.com/images/tomato.jpg'),
        Product(product_name='Cucumber', description='Crisp and crunchy', price='1.75', quantity='150', product_image='https://example.com/images/cucumber.jpg'),
        Product(product_name='Carrot', description='Rich in vitamins', price='1.00', quantity='200', product_image='https://example.com/images/carrot.jpg'),
        Product(product_name='Lettuce', description='Great for salads', price='1.25', quantity='80', product_image='https://example.com/images/lettuce.jpg'),
        Product(product_name='Potato', description='Earthy flavor', price='0.75', quantity='300', product_image='https://example.com/images/potato.jpg'),
    ]


    customers = [
        Customer(first_name='John', last_name='Doe', location='City Center', email='john.doe@mail.com', phone='+1-555-0001'),
        Customer(first_name='Jane', last_name='Smith', location='Uptown', email='jane.smith@mail.com', phone='+1-555-0002'),
        Customer(first_name='Mike', last_name='Johnson', location='Downtown', email='mike.johnson@mail.com', phone='+1-555-0003'),
        Customer(first_name='Sara', last_name='Williams', location='Suburbs', email='sara.williams@mail.com', phone='+1-555-0004'),
        Customer(first_name='Tom', last_name='Brown', location='Lakeside', email='tom.brown@mail.com', phone='+1-555-0005'),
    ]

    
    farmer_products = [
        FarmerProduct(farmer_id=1, product_id=1),  
        FarmerProduct(farmer_id=1, product_id=2),  
        FarmerProduct(farmer_id=2, product_id=3),  
        FarmerProduct(farmer_id=3, product_id=4),  
        FarmerProduct(farmer_id=4, product_id=5),  
    ]

  
    orders = [
        Order(quantity=5, product_id=1, customer_id=1),  
        Order(quantity=3, product_id=2, customer_id=2),  
        Order(quantity=1, product_id=3, customer_id=3),  
        Order(quantity=10, product_id=4, customer_id=4), 
        Order(quantity=2, product_id=5, customer_id=5),  
    ]

   
    db.session.add_all(farmers)
    db.session.commit()

   
    db.session.add_all(products)
    db.session.commit()

    db.session.add_all(customers)
    db.session.commit()

    #
    db.session.add_all(farmer_products)
    db.session.commit()


    db.session.add_all(orders)
    db.session.commit()

    print('Database seeded successfully!')
