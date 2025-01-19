import { useNavigate } from "react-router-dom";
import { useAuth } from "../provider/authProvider";

const Logout = () => {
  const { setToken, setUser } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    setUser();
    setToken();
    
    navigate("/", { replace: true });
  };

  setTimeout(() => {
    handleLogout();
  }, 0.5 * 1000);

  return <>Logout Page</>;
};

export default Logout;
