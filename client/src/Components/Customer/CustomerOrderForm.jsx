// src/components/Customer/CustomerOrderForm.jsx
import { useFormik } from 'formik';
import axios from 'axios';

const CustomerOrderForm = ({ productId }) => {
  const formik = useFormik({
    initialValues: {
      quantity: 1,
    },
    onSubmit: async (values) => {
      try {
        // API call to place an order
        const response = await axios.post('http://localhost:5000/orders', {
          product_id: productId,
          quantity: values.quantity,
        });
        console.log('Order placed successfully:', response.data);
      } catch (error) {
        console.error('Error placing order:', error);
      }
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <label htmlFor="quantity">Quantity</label>
      <input
        id="quantity"
        type="number"
        {...formik.getFieldProps('quantity')}
      />

      <button type="submit">Place Order</button>
    </form>
  );
};

export default CustomerOrderForm;
