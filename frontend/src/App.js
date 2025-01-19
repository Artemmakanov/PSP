import AuthProvider from "./provider/authProvider";
import Routes from "./routes";
import NavigationBar from "./components/NavigationBar"

function App() {
  return (
    <AuthProvider>
      <NavigationBar>
        <Routes />
      </NavigationBar>
    </AuthProvider>
  );
}

export default App;
