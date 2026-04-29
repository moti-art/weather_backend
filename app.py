from flask import Flask, jsonify
import requests
import os
from urllib.parse import quote

app = Flask(__name__)

API_KEY = os.getenv('OPENWEATHER_API_KEY')
TRACKER_URL = "http://weather-tracker:5001/track"

@app.route('/weather/<location_key>')
def get_weather(location_key):
    location_safe = quote(location_key)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location_safe}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), response.status_code

    result = {
        "location": location_key,
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }

    # שליחה לטרקר
    try:
        requests.post(TRACKER_URL, json={"city": location_key}, timeout=1)
    except Exception as e:
        print(f"Tracker failed: {e}")

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)