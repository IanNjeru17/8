// src/components/Customer/CustomerProductList.jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

const CustomerProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch all available products
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://localhost:5000/products');
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Available Products</h2>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            {product.name} - ${product.price} (Quantity: {product.quantity})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CustomerProductList;
