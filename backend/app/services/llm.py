import os

import requests

OLLAMA_URL = "http://localhost:11434"


def parse(text: str):
    res = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": f"""
                Extract food names and calories from text.
                You can make food names shorter and more general. For examples: pasta carbonara with cheese -> pasta.
                Return ONLY JSON: {{"food_name": string or null, "calories": number or null}}

                Text: {text}
                """,
            "stream": False,
        },
    )

    return res.json()["response"]
