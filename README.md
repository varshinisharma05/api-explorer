<img width="1919" height="901" alt="image" src="https://github.com/user-attachments/assets/93e56a36-69e8-443a-a8d6-1057ef4e6b36" />
# 🌐 API Explorer

API Explorer is a full-stack web application built to practice working with real-world APIs, backend development, and database integration.

This app acts as a **central hub** where users can search for:

* 🌍 Country information
* ⛅ Weather details
* 🥘 Recipes

Instead of visiting multiple websites, everything is accessible in one place through a clean interface.

---

## 🚀 Features

* 🌍 **Country Search**

  * Get capital, region, and population using the RestCountries API
<img width="1884" height="885" alt="image" src="https://github.com/user-attachments/assets/a7022134-8395-4992-bc91-bfe5ba7ea9c8" />

* ⛅ **Weather Search**

  * Real-time temperature, humidity, and conditions using OpenWeatherMap API
    <img width="1902" height="903" alt="image" src="https://github.com/user-attachments/assets/c5435620-dfb8-4561-9da0-2c822e8de888" />


* 🥘 **Recipe Search**

  * Search recipes by ingredient with images using TheMealDB API
  <img width="1901" height="826" alt="image" src="https://github.com/user-attachments/assets/4e26675c-f143-416f-8319-9fcd42b5ca21" />


* 🕒 **Search History (MySQL)**

  * All user searches are stored in a MySQL database
  * Helps track and display previous queries
<img width="1299" height="907" alt="image" src="https://github.com/user-attachments/assets/55be7e97-c104-412b-952a-bf4c6ac40cc9" />

---

## 🛠️ Tech Stack
<img width="216" height="354" alt="Screenshot 2026-03-15 151342" src="https://github.com/user-attachments/assets/a4bfcc56-4a18-4a7d-8d58-dc2303b864ed" />


### Frontend

* HTML
* CSS
* JavaScript (jQuery)
* Bootstrap

### Backend

* Python (Flask)
* REST API handling using `requests`

### Database

* MySQL (hosted on Railway)
* `mysql-connector-python` for database connection

### Deployment

* Hosted on **Railway**
* Gunicorn used as production server

### Environment Management

* `python-dotenv` for secure API key handling

---

## 🌍 Deployment (Railway)

This project is deployed using Railway with:

* A **MySQL database service**
* Environment variables stored securely in Railway dashboard
* Backend served using:

```bash
gunicorn app:app
```

### Environment Variables Used

```env
DB_HOST=your_railway_host
DB_PORT=your_port
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=your_database_name
WEATHER_API_KEY=your_api_key
```

---

## 🧗 Challenges Faced

### 🔐 1. API Key Security

Accidentally exposed an API key during early development.
Learned to:

* Use `.env` files
* Add `.env` to `.gitignore`
* Store secrets in Railway instead of code

---

### 🧩 2. Handling API Errors
<img width="1895" height="962" alt="image" src="https://github.com/user-attachments/assets/da9cc494-35ac-4b2d-8945-46d915a7d8b2" />


Issues faced:

* UI showing old data on failed searches
* Empty responses breaking layout

Solution:

* Added proper error handling
* Cleared UI before rendering new data

---

### 🗄️ 3. MySQL Integration (Railway)

Challenges:

* Connecting Flask to Railway MySQL instance
* Handling host, port, and credentials correctly

Learned:

* How cloud databases work
* Importance of environment variables

---

### 🔄 4. Parsing Different APIs

Each API had different JSON structures:

* Nested objects
* Arrays inside objects

Improved skills in:

* JSON parsing
* Conditional rendering

---

## 💻 How to Run Locally

### 1. Clone the Repository

```bash
git clone <your-repo-link>
cd api-explorer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env` File

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=your_db
WEATHER_API_KEY=your_api_key
```

### 4. Run the App

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000
```

---

## 📚 What I Learned

* Building a complete full-stack application from scratch
* Working with multiple external APIs
* Handling backend logic using Flask
* Connecting and managing a MySQL database
* Deploying apps and databases using Railway
* Writing cleaner, structured code

---

## 📌 Future Improvements

* Add user authentication (login/signup)
* Improve UI/UX design
* Add pagination for recipes
* Convert to React frontend
* Add caching for faster API responses

---

## 🏁 Conclusion

This project is a major step in my journey toward becoming a full-stack developer.
It helped me understand how frontend, backend, APIs, and databases all connect together in a real-world application.

---

