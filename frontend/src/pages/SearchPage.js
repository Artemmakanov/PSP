import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { BASE_URL } from "./const"

const SearchPage = () => {
  const [query, setQuery] = useState("");
  const [articles, setArticles] = useState([]);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleSearch = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await fetch(`${BASE_URL}/search?q=${query}`);
      if (!response.ok) throw new Error("Ошибка поиска");

      const data = await response.json();
      setArticles(data);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="search-container">
      <h2>Поиск статей</h2>
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSearch}>
        <input
          type="text"
          placeholder="Введите запрос"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          required
        />
        <button type="submit">Поиск</button>
      </form>
      <ul className="article-list">
        {articles.map((article) => (
          <li key={article.id} onClick={() => navigate(`/article/${article.id}`)}>
            {article.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SearchPage;
