// src/components/Farmer/FarmerProductForm.jsx
import { useFormik } from 'formik';
import * as Yup from 'yup';
import axios from 'axios';

const FarmerProductForm = () => {
  const formik = useFormik({
    initialValues: {
      name: '',
      description: '',
      price: '',
      quantity: '',
    },
    validationSchema: Yup.object({
      name: Yup.string().required('Product name is required'),
      price: Yup.number().required('Price is required').positive('Price must be positive'),
      quantity: Yup.number().required('Quantity is required').min(1, 'At least 1 item must be available'),
    }),
    onSubmit: async (values) => {
      try {
        // API call to backend to add product
        const response = await axios.post('http://localhost:5000/products', values);
        console.log('Product added successfully:', response.data);
      } catch (error) {
        console.error('Error adding product:', error);
      }
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <label htmlFor="name">Product Name</label>
      <input
        id="name"
        type="text"
        {...formik.getFieldProps('name')}
      />
      {formik.touched.name && formik.errors.name ? <div>{formik.errors.name}</div> : null}

      <label htmlFor="description">Description</label>
      <textarea
        id="description"
        {...formik.getFieldProps('description')}
      />

      <label htmlFor="price">Price</label>
      <input
        id="price"
        type="number"
        {...formik.getFieldProps('price')}
      />
      {formik.touched.price && formik.errors.price ? <div>{formik.errors.price}</div> : null}

      <label htmlFor="quantity">Quantity Available</label>
      <input
        id="quantity"
        type="number"
        {...formik.getFieldProps('quantity')}
      />
      {formik.touched.quantity && formik.errors.quantity ? <div>{formik.errors.quantity}</div> : null}

      <button type="submit">Add Product</button>
    </form>
  );
};

export default FarmerProductForm;
