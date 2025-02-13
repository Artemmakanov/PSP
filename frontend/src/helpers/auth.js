// src/helpers/auth.js

// Сохранение токена в localStorage
export function saveToken(token) {
  localStorage.setItem("jwt_token", token);
}

// Получение токена из localStorage
export function getToken() {
  return localStorage.getItem("jwt_token");
}

// Удаление токена
export function removeToken() {
  localStorage.removeItem("jwt_token");
}

// Проверка авторизации
export function isAuthenticated() {
  return !!getToken();
}