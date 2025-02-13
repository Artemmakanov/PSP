import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { BASE_URL } from "./const"

const UserPage = () => {
  const { login } = useParams();
  const [favorites, setFavorites] = useState([]);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchFavorites = async () => {
      try {
        const response = await fetch(`${BASE_URL}/get_users_papers?login=${login}`);
        if (!response.ok) throw new Error("Ошибка загрузки избранного");
        const data = await response.json();
        setFavorites(data);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchFavorites();
  }, [login]);

  return (
    <div className="user-container">
      <h2>Статьи пользователя {login}</h2>
      {error && <p className="error">{error}</p>}
      <ul>
        {favorites.map((article) => (
          <li key={article.id} onClick={() => navigate(`/article/${article.id}`)}>
            {article.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserPage;
