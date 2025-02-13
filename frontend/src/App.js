
import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { getToken } from "./helpers/auth";
import Navbar from "./components/Navbar";
import Authorization from "./pages/Authorization";
import Registration from "./pages/Registration";
import ProtectedRoute from "./pages/ProtectedRoute";

function App() {
  const [user, setUser] = useState(null);

  return (
    <Router>
      <Navbar user={user} />
      <Routes>
        <Route path="/login" element={<Authorization setUser={setUser} />} />
        <Route path="/register" element={<Registration />} />
        <Route
          path="/protected"
          element={
            getToken() ? <ProtectedRoute user={user} /> : <Navigate to="/login" />
          }
        />
        <Route path="*" element={<Navigate to="/protected" />} />
      </Routes>
    </Router>
  );
}

export default App;