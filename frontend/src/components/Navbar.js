
import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { getToken, removeToken } from "../helpers/auth";

function Navbar({ user }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    removeToken();
    navigate("/login");
  };

  return (
    <nav className="navbar">
      <ul>
        <li><Link to="/protected">Protected Route</Link></li>
        <li><Link to="/login">Authorization</Link></li>
        <li><Link to="/register">Registration</Link></li>
      </ul>

      {user ? (
        <div className="user-info">
          <span>{user.fullName} ({user.login})</span>
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : null}
    </nav>
  );
}

export default Navbar;
