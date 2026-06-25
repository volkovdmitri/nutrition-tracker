import { Route, Routes } from "react-router-dom";
import Login from "./Login.jsx";
import Profile from "./Profile.jsx";

function App() {
	return (
		<Routes>
			<Route path="/profile" element={<Profile />} />
			<Route path="/login" element={<Login />} />
		</Routes>
	);
}

export default App;
