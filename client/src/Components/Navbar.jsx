// src/components/Navbar.jsx
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/">Home</Link></li>
        <li><Link to="/farmer">Farmer</Link></li>
        <li><Link to="/customer">Customer</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
