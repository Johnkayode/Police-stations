import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def geocode(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json?components=country:ng"
    payload = {
            "address": str(address) + "Ijebu Ode",
            "key": os.getenv("GOOGLE_API_KEY")
    }

    try:
        r = requests.get(url, params=payload, timeout=10)
    except Exception as e:
        raise e

    resp = json.loads(r.text)
    results = resp["results"]
    if results:
        return {
            "address": results[0]['formatted_address'],
            "latitude": results[0]['geometry']['location']['lat'],
            "longitude": results[0]['geometry']['location']['lng']
        }

    return {"error":"Address Not Found"}



