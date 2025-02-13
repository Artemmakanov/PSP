
import React, { useState } from "react";
import { login } from "../api/auth";
import { saveToken } from "../helpers/auth";
import { useNavigate } from "react-router-dom";

function Authorization({ setUser }) {
  const [loginData, setLoginData] = useState({ login: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setLoginData({ ...loginData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const { token } = await login(loginData);
      saveToken(token);
      setUser({ login: loginData.login, fullName: "Демо Юзер" }); // TODO: заменить демо-данные
      navigate("/protected");
    } catch (err) {
      alert("Авторизация не удалась: " + err.message);
    }
  };

  return (
    <div className="page">
      <h2>Authorization</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Login:
          <input
            type="text"
            name="login"
            value={loginData.login}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={loginData.password}
            onChange={handleChange}
            required
          />
        </label>
        <br />
        <button type="submit">Log In</button>
      </form>
    </div>
  );
}

export default Authorization;