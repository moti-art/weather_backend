from flask import Flask, jsonify
import requests
import os
from urllib.parse import quote

app = Flask(__name__)

# קבלת מפתח ה-API מהסביבה
API_KEY = os.getenv('OPENWEATHER_API_KEY')

# כתובת הטרקר בתוך הקלאסטר (משתמש ב-DNS הפנימי של קוברנטיס)
TRACKER_URL = "http://weather-tracker:5001/track"

@app.route('/weather/<location_key>')
def get_weather(location_key):
    # טיפול ברווחים עבור ה-API של OpenWeather
    location_safe = quote(location_key)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location_safe}&appid={API_KEY}&units=metric"

    # פנייה ל-OpenWeather
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

    # --- שליחת נתונים ל-Tracker (החלק החדש) ---
    try:
        # שליחת בקשת POST לטרקר עם שם העיר
        # הגדרנו timeout של שנייה אחת כדי לא לעכב את המשתמש
        requests.post(TRACKER_URL, json={"city": location_key}, timeout=1)
    except Exception as e:
        # אם הטרקר לא זמין, רק נדפיס ללוג של הפוד - האתר ימשיך לעבוד כרגיל
        print(f"Logging to tracker failed for {location_key}: {e}")

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)