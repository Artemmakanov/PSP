const BASE_URL = "http://localhost:5000";

// Функция для авторизации
export async function login({ login, password }) {
  const response = await fetch(`${BASE_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ login, password }),
  });

  if (!response.ok) throw new Error("Неверный логин/пароль");
  return response.json(); // Вернет { token }
}

// Функция для регистрации
export async function register(userData) {
  const response = await fetch(`${BASE_URL}/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(userData),
  });

  if (!response.ok) throw new Error("Такой логин уже существует");
  return response.json(); // Вернет успех
}

// Функция проверки защищенного route
export async function checkProtected(token) {
  const response = await fetch(`${BASE_URL}/protected`, {
    method: "GET", 
    headers: { Authorization: `${token}` },
  });

  if (!response.ok) throw new Error("Не авторизован");
  return response.json();
}
