import { RouterProvider, createBrowserRouter } from "react-router-dom";
import { useAuth } from "../provider/authProvider";
import { ProtectedRoute } from "./ProtectedRoute";
import Authorization from "../pages/Authorization"
import Registration from "../pages/Registration"
import Search from "../pages/Search"

const Routes = () => {
  const { token } = useAuth();

  // Define public routes accessible to all users
  const routesForPublic = [
    {
      path: "/authorization",
      element: <Authorization/>,
    },
    {
      path: "/registration",
      element: <Registration/>,
    },
  ];

  // Define routes accessible only to authenticated users
  const routesForAuthenticatedOnly = [
    {
      path: "/",
      element: <ProtectedRoute />, // Wrap the component in ProtectedRoute
      children: [
        {
          path: "/search",
          element: <Search/>,
        },
      ],
    },
  ];

  // Combine and conditionally include routes based on authentication status
  const router = createBrowserRouter([
    ...routesForPublic,
    ...routesForAuthenticatedOnly,
  ]);

  // Provide the router configuration using RouterProvider
  return <RouterProvider router={router} />;
};

export default Routes;
