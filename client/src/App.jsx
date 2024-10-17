// import React from 'react';
// import Home from "./Components/Home.jsx"; 

// function App() {
//   return (
//     <div className="App">
//       <Home />
//     </div>
//   );
// }

// export default App;
// src/App.jsx
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Components/Navbar.jsx'
import Home from './Components/Home.jsx';
import FarmerDashboard from './Components/Farmer/FarmerDashboard.jsx';
import CustomerProductList from './Components/Customer/CustomerProductList.jsx';



function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/farmer" element={<FarmerDashboard />} />
        <Route path="/customer" element={<CustomerProductList />} />
      </Routes>
    </Router>
  );
}

export default App;
