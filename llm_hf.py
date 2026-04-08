import requests
import time
from config import HF_API_KEY, MODEL_URL

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def query_huggingface(prompt):
    for attempt in range(3):
        try:
            response = requests.post(
                MODEL_URL,
                headers=headers,
                json={
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 500,
                        "temperature": 0.5,
                        "return_full_text": False
                    }
                },
                timeout=60
            )

            # Handle HTTP errors
            if response.status_code != 200:
                print("HTTP ERROR:", response.status_code)
                print(response.text)
                time.sleep(2)
                continue

            # Safe JSON parsing
            try:
                data = response.json()
            except Exception:
                print("❌ Non-JSON response:")
                print(response.text)
                time.sleep(2)
                continue

            # Handle HF errors
            if isinstance(data, dict) and "error" in data:
                print("HF Error:", data["error"])
                time.sleep(3)
                continue

            if isinstance(data, list):
                return data[0].get("generated_text", "")

            return str(data)

        except Exception as e:
            print("Request failed:", e)
            time.sleep(2)

    return "❌ Failed to get response from Hugging Face"


def generate_content(text):
    # ✅ STEP 2: limit size (CRITICAL FIX)
    text = text[:1500]

    prompt = f"""
Summarize and structure this transcript:

1. Bullet summary (5 points)
2. Article with headings:
   - Introduction
   - Key Concepts
   - Insights
   - Conclusion

Transcript:
{text}
"""
    return query_huggingface(prompt)