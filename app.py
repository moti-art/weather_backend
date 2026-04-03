from flask import Flask, jsonify
import requests
import os
from urllib.parse import quote # הוספנו את זה לטיפול ברווחים

app = Flask(__name__)

API_KEY = os.getenv('OPENWEATHER_API_KEY')

@app.route('/weather/<location_key>')
def get_weather(location_key):
    # כאן אנחנו מוודאים שרווחים יהפכו ל-%20 עבור ה-API
    location_safe = quote(location_key)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location_safe}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": "City not found or API key not active"}), response.status_code

    result = {
        "location": location_key,
        "temperature": data['main']['temp'],
        "description": data['weather'][0]['description'],
        "humidity": data['main']['humidity'],
        "wind_speed": data['wind']['speed']
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)