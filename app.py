from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "c1536adsf5d5fa1dd5d6df33654b35c3751525256263222222325225"  # 🔑 Replace with your OpenWeatherMap API key

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url).json()

            if response.get("cod") != 200:
                error_message = "❌ City not found. Please try again."
            else:
                weather_data = {
                    "city": response["name"],
                    "temperature": response["main"]["temp"],
                    "description": response["weather"][0]["description"].capitalize(),
                    "icon": response["weather"][0]["icon"]
                }
        else:
            error_message = "⚠️ Please enter a city."

    return render_template("index.html", weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
