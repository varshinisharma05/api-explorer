from flask import Flask, render_template, jsonify
import requests
import os
import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database credentials
DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

app = Flask(__name__)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# -----------------------------------------
# Safe DB connection
# -----------------------------------------
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connection_timeout=5
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        return None


# -----------------------------------------
# Save API request
# -----------------------------------------
def save_request(api_type, query_value):

    conn = get_db_connection()

    if conn is None:
        return

    cursor = conn.cursor()

    try:
        sql = "INSERT INTO api_requests (api_type, query_value) VALUES (%s, %s)"
        cursor.execute(sql, (api_type, query_value))
        conn.commit()
    except Exception as e:
        print("Insert failed:", e)

    cursor.close()
    conn.close()


# -----------------------------------------
# Home page
# -----------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------------------
# Country API
# -----------------------------------------
@app.route("/api/country/<country_name>")
def get_country(country_name):

    save_request("country", country_name)

    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)
    data = response.json()

    country = data[0]

    result = {
        "country": country["name"]["common"],
        "capital": country["capital"][0],
        "region": country["region"],
        "population": country["population"]
    }

    return jsonify(result)


# -----------------------------------------
# Weather API
# -----------------------------------------
@app.route("/api/weather/<city>")
def get_weather(city):

    save_request("weather", city)

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    result = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"]
    }

    return jsonify(result)


# -----------------------------------------
# Recipe API
# -----------------------------------------
@app.route("/api/recipe/<food>")
def get_recipe(food):

    save_request("recipe", food)

    url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={food}"

    response = requests.get(url)
    data = response.json()

    meals = data.get("meals")

    if not meals:
        return jsonify({"error": "No recipes found"}), 404

    results = []

    for meal in meals[:6]:
        results.append({
            "name": meal["strMeal"],
            "image": meal["strMealThumb"]
        })

    return jsonify(results)


# -----------------------------------------
# Search history
# -----------------------------------------
@app.route("/api/history")
def get_history():

    conn = get_db_connection()

    if conn is None:
        return jsonify([])

    cursor = conn.cursor()

    query = """
    SELECT api_type, query_value, created_at
    FROM api_requests
    ORDER BY created_at DESC
    LIMIT 10
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    history = []

    for row in rows:
        history.append({
            "type": row[0],
            "query": row[1],
            "time": str(row[2])
        })

    cursor.close()
    conn.close()

    return jsonify(history)


# -----------------------------------------
# Health check
# -----------------------------------------
@app.route("/health")
def health():
    return "API Explorer running!"


# -----------------------------------------
# Run server locally
# -----------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)