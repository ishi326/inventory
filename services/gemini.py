"""
GEMINI implementation for extracting inventory from photos of handwritten or printed inventory count sheets.
Returns a JSON array of objects with the shape: [{"sku": "<one of the valid SKU names>", "quantity": <integer>}].
"""

import os
import json
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent"

def extract_inventory_from_photo(photo_bytes: bytes, content_type: str, known_skus: list[str]) -> list[dict]:
    base64_image = base64.b64encode(photo_bytes).decode("utf-8")
    sku_list_text = ", ".join(known_skus)

    prompt = (
        "This image is a handwritten or printed inventory count sheet. "
        f"The valid SKU names are exactly: {sku_list_text}. "
        "Match every row to the closest one of these, even if handwriting is messy. "
        "Return ONLY a JSON array, no markdown, no commentary, in this shape: "
        '[{"sku": "<one of the valid SKU names above>", "quantity": <integer>}]. '
        "If a quantity is illegible, use -1."
    )

    payload = {
        "contents": [{
            "parts": [
                {"text": prompt},
                {"inline_data": {"mime_type": content_type, "data": base64_image}}
            ]
        }]
    }

    response = requests.post(f"{GEMINI_URL}?key={GEMINI_API_KEY}", json=payload)
    response.raise_for_status()
    result = response.json()

    text = result["candidates"][0]["content"]["parts"][0]["text"]
    cleaned = text.replace("```json", "").replace("```", "").strip()
    return json.loads(cleaned)