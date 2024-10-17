import React from 'react';
import '../Styles/Home.css';

const Home = () => {
  return (
    <div className="container">
      {/* Header Section */}
      <header className="header">
        <div className="logo">
          <img src="../logo.png" alt="Agrilink logo" className="logo-img" />
          <h1>AGRILINK</h1>
          <p>Sow Success</p>
        </div>
      </header>

      {/* Welcome Section */}
      <section className="welcome-section">
        <h2>Welcome to the Modern Farming Era</h2>
        <button className="learn-button">Learn</button>
        <div className="icons">
          <img src="vegetable-icon.png" alt="Vegetables" />
          <img src="corn-icon.png" alt="Corn" />
        </div>
      </section>

      {/* Products Section */}
      <section className="products">
        <div className="product-card">
          <h3>Organic Vegetables</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt.</p>
        </div>
        <div className="product-card">
          <h3>Organic Fruits</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt.</p>
        </div>
      </section>

      {/* About Section */}
      <section className="about-section">
        <img src="../jaba.jpeg" alt="Farmer" className="farmer-img" />
        <div className="about-text">
          <h3>About us</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut labore et dolore magna aliqua.</p>
        </div>
      </section>

      {/* Agro Culture Section */}
      <section className="culture-section">
        <h3>Agro Culture</h3>
        <div className="culture-icons">
          <img src="plant-icon.png" alt="Plant" />
          <img src="clover-icon.png" alt="Clover" />
          <img src="user-icon.png" alt="User" />
        </div>
      </section>
    </div>
  );
};

export default Home;

