// src/components/Farmer/FarmerDashboard.jsx
import FarmerProductForm from './FarmerProductForm';
import FarmerProductList from './FarmerProductList';

const FarmerDashboard = () => {
  return (
    <div>
      <h2>Farmer Dashboard</h2>
      <FarmerProductForm />
      <FarmerProductList />
    </div>
  );
};

export default FarmerDashboard;
