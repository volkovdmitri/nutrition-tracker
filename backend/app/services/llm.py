import json

import requests  # type: ignore[import-untyped]

OLLAMA_URL = "http://ollama:11434"


def parse(text: str):
    res = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": f"""
                Extract food names and calories from text.
                You can make food names shorter and more general.
                Try to return at least some non null food_name.
                Return ONLY JSON: {{"food_name": string or null, "calories": number or null}}

                Text: {text}
                """.strip(),
            "stream": False,
        },
    )
    text = res.json()["response"]
    text = text.replace("```json", "").replace("```", "").strip()
    result = json.loads(text)
    return result
