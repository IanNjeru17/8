// src/components/Farmer/FarmerProductList.jsx
import { useState, useEffect } from 'react';
import axios from 'axios';

const FarmerProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products owned by the farmer
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://localhost:5000/farmer/products');
        setProducts(response.data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      <h3>Your Products</h3>
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

export default FarmerProductList;
