
import React, { useEffect, useState } from "react";
import { checkProtected } from "../api/auth";
import { useNavigate } from "react-router-dom";

function ProtectedRoute({ user }) {
  const [data, setData] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchData() {
      try {
        const token = localStorage.getItem("jwt_token");
        const response = await checkProtected(token);
        setData(response); // Например, можно отобразить данные из авторизированного запроса
      } catch (err) {
        alert("Доступ запрещён!"); // В случае ошибки, перенаправим на авторизацию
        navigate("/login");
      }
    }
    fetchData();
  }, [navigate]);

  return (
    <div className="page">
      <h2>Protected Route</h2>
      {data ? (
        <div>
          <p>Данные для авторизованного пользователя:</p>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      ) : (
        <p>Загрузка...</p>
      )}
      {user && (
        <p>
          Добро пожаловать, {user.fullName} ({user.login})!
        </p>
      )}
    </div>
  );
}

export default ProtectedRoute;