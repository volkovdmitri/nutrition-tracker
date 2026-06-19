import { useState } from 'react'

function App() {
  const [foods, setFoods] = useState([]);
  const [loading, setLoading] = useState(false);

  async function fetchFoods() {
    setLoading(true);

    try {
      const response = await fetch("http://api:8000/food");
      
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
    <div style={{ padding: 20, fontFamily: "Arial" }}>
      <h1>Nutrition Tracker</h1>

      <button onClick={fetchFoods}>
        Load foods from DB
      </button>

      {loading && <p>Loading...</p>}

      <h2>Foods:</h2>

      {foods.length === 0 && !loading && (
        <p>No data</p>
      )}

      <ul>
        {foods.map((food) => (
          <li key={food.id}>
            {food.food_name} — {food.calories} kcal
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
