import { useNavigate } from "react-router-dom";

function Login() {
	const navigate = useNavigate();

	const handleLogin = () => {
		navigate("/profile");
	};

	return (
		<div className="container">
			<h2>Login Page</h2>
			<button type="button" onClick={handleLogin}>
				Login
			</button>
		</div>
	);
}

export default Login;
