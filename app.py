from flask import Flask, render_template, request
import pickle
import numpy as np
import mysql.connector
from urllib.parse import urlparse

app = Flask(__name__)

# ----------------------------
# Load Trained Model
# ----------------------------
model = pickle.load(open("model/phishing_model.pkl", "rb"))

# ----------------------------
# Database Connection
# ----------------------------
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Chitty@6543",
        database="phishing_db"
    )
    cursor = db.cursor()
    print("Database connected successfully!")
except Exception as e:
    print("Database connection failed:", e)


# ----------------------------
# Basic URL Feature Extraction
# ----------------------------
def extract_features(url):
    features = []

    features.append(1 if len(url) < 75 else -1)
    features.append(-1 if "@" in url else 1)
    features.append(-1 if "//" in url[8:] else 1)

    domain = urlparse(url).netloc
    features.append(-1 if "-" in domain else 1)

    features.append(1 if url.startswith("https") else -1)

    while len(features) < 30:
        features.append(1)

    return np.array([features])


# ----------------------------
# Home Route
# ----------------------------
@app.route('/')
def home():
    return render_template("index.html")


# ----------------------------
# Prediction Route
# ----------------------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        url = request.form.get('url')

        if not url:
            return render_template("index.html", prediction_text="Please enter a URL")

        final_features = extract_features(url)
        prediction = model.predict(final_features)

        if prediction[0] == 1:
            result = "Phishing Website"
        else:
            result = "Legitimate Website"

        # Save to database
        sql = "INSERT INTO predictions (result) VALUES (%s)"
        cursor.execute(sql, (result,))
        db.commit()

        print("Prediction result:", result)  # debug line

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        print("Error:", e)
        return render_template("index.html", prediction_text="Error in prediction")


# ----------------------------
# Prediction History Route
# ----------------------------
@app.route('/history')
def history():
    cursor.execute("SELECT * FROM predictions ORDER BY id DESC")
    records = cursor.fetchall()
    return render_template("history.html", records=records)


# ----------------------------
# Analytics Dashboard Route
# ----------------------------
@app.route('/dashboard')
def dashboard():
    cursor.execute("SELECT COUNT(*) FROM predictions")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM predictions WHERE result LIKE '%Phishing%'")
    phishing_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM predictions WHERE result LIKE '%Legitimate%'")
    legit_count = cursor.fetchone()[0]

    phishing_percentage = round((phishing_count / total) * 100, 2) if total > 0 else 0

    return render_template(
        "dashboard.html",
        total=total,
        phishing_count=phishing_count,
        legit_count=legit_count,
        phishing_percentage=phishing_percentage
    )


# ----------------------------
# Run Application
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
