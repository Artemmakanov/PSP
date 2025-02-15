import { useEffect, useState } from "react";
import { useContext } from "react";

import { useParams, useNavigate } from "react-router-dom";
import { BASE_URL } from "./const"
import { AuthContext } from "../context/AuthContext";


const ArticlePage = () => {
  const { user } = useContext(AuthContext);
  const { id } = useParams();
  const [article, setArticle] = useState(null);
  const [recommendations, setRecommendations] = useState([]);
  const [favoriteUsers, setFavoriteUsers] = useState([]);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const resArticle = await fetch(`${BASE_URL}/page?id=${id}`);
        if (!resArticle.ok) throw new Error("Ошибка загрузки статьи");
        const articleData = await resArticle.json();
        console.log(articleData)

        const resRecs = await fetch(`${BASE_URL}/get_similar?id=${id}`);
        if (!resRecs.ok) throw new Error("Ошибка загрузки рекомендаций");
        const recsData = await resRecs.json();

        const resUsers = await fetch(`${BASE_URL}/get_paper_users?id=${id}`);
        if (!resUsers.ok) throw new Error("Ошибка загрузки пользователей");
        const usersData = await resUsers.json();

        setArticle(articleData);
        setRecommendations(recsData);
        setFavoriteUsers(usersData);
      } catch (err) {
        setError(err.message);
      }
    };

    fetchData();
  }, [id]);

  const handleFavorite = async () => {
    // Здесь должна быть логика добавления в избранное (если поддерживается backend)
    await fetch(`${BASE_URL}/add_paper_to_favourites?login=${user.login}&id=${id}`, {method: "POST"});
  };

  return (
    <div className="article-container">
      {error && <p className="error">{error}</p>}
      {article && (
        <>
          <h2>{article.title}</h2>
          <h2>{article.link}</h2>
          <iframe src={article.pdf_url} title="PDF статьи"></iframe>
          <button onClick={handleFavorite}>Добавить в избранное</button>
          <h3>Рекомендации</h3>
          <ul>
            {recommendations.map((rec) => (
              <li key={rec.id} onClick={() => navigate(`/article/${rec.id}`)}>
                {rec.title}
              </li>
            ))}
          </ul>
          <h3>Добавили в избранное</h3>
          <ul>
            {favoriteUsers.map((login) => (
              <li key={login} onClick={() => navigate(`/user/${login}`)}>
                {login}
              </li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
};

export default ArticlePage;
