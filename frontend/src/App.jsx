import { useState } from "react";
import "./App.css";
import { DotLottieReact } from "@lottiefiles/dotlottie-react";

function App() {
	const [showMascot, setShowMascot] = useState(false);
	const [message, setMessage] = useState("Привет!");

	const [foodName, setFoodName] = useState("");
	const [calories, setCalories] = useState("");
	const [text, setText] = useState("");

	const [foods, setFoods] = useState([]);
	const [loading, setLoading] = useState(false);

	const messages = [
		"Ты отлично справляешься",
		"Хорошая работа",
		"Так держать",
		"Ты двигаешься правильно",
		"Отличный прогресс",
		"Я тобой доволен",
		"Становится лучше с каждым шагом",
		"Аккуратно и стабильно",
		"Ты на верном пути",
		"Продолжай в том же духе",
	];
	const getRandomMessage = () => {
		return messages[Math.floor(Math.random() * messages.length)];
	};

	const Mascot = () => {
		return (
			showMascot && (
				<div className="mascot-wrapper">
					<div className="speech-bubble">{message}</div>
					<div className="mascot">
						<DotLottieReact
							src="/src/assets/mascot.lottie"
							autoplay
							loop
							style={{
								width: "100%",
								height: "100%",
								display: "block",
							}}
						/>
					</div>
				</div>
			)
		);
	};

	async function handleTextSubmit() {
		await fetch("http://127.0.0.1:8000/text", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				text: text,
			}),
		});

		setText("");
		setMessage(getRandomMessage());
		setShowMascot(true);
	}

	async function handleSubmit() {
		await fetch("http://127.0.0.1:8000/food", {
			method: "POST",
			headers: {
				"Content-Type": "application/json",
			},
			body: JSON.stringify({
				food_name: foodName,
				calories: Number(calories),
			}),
		});

		setFoodName("");
		setCalories("");
		setMessage(getRandomMessage());
		setShowMascot(true);
	}

	async function fetchFoods() {
		setLoading(true);

		try {
			const response = await fetch("http://127.0.0.1:8000/food");

			if (!response.ok) {
				throw new Error("Request failed");
			}

			const data = await response.json();
			console.log("asdas");

			setFoods(data);
		} catch (error) {
			console.error("Error:", error);
		} finally {
			setLoading(false);
		}
		setMessage(getRandomMessage());
		setShowMascot(true);
	}

	return (
		<div className="container">
			<div className="mascot">
				<Mascot />
			</div>
			{/* LEFT UP*/}
			<div className="left">
				<h2>Submit food</h2>

				<input
					value={foodName}
					onChange={(e) => setFoodName(e.target.value)}
					placeholder="Food name"
				/>

				<input
					value={calories}
					onChange={(e) => setCalories(e.target.value)}
					placeholder="Calories"
					type="number"
				/>

				<button type="button" onClick={handleSubmit}>
					Submit
				</button>
			</div>

			{/* LEFT BOTTOM*/}
			<div className="left">
				<h2>Submit text</h2>

				<input
					value={text}
					onChange={(e) => setText(e.target.value)}
					placeholder="Text"
				/>

				<button type="button" onClick={handleTextSubmit}>
					Submit
				</button>
			</div>

			{/* RIGHT */}
			<div className="right">
				<h2>Database</h2>

				<button type="button" onClick={fetchFoods}>
					Get data
				</button>
				{loading && <p>Loading...</p>}
				{foods.length === 0 && !loading && <p>No data</p>}
				<ul>
					{foods.map((food) => (
						<li key={food.id}>
							{food.food_name} — {food.calories} kcal
						</li>
					))}
				</ul>
			</div>
		</div>
	);
}

export default App;
