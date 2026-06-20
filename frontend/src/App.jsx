import { useState } from "react";
import "./App.css";

function App() {
	const [foodName, setFoodName] = useState("");
	const [calories, setCalories] = useState("");

	const [foods, setFoods] = useState([]);
	const [loading, setLoading] = useState(false);

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
	}

	return (
		<div className="container">
			{/* LEFT */}
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
