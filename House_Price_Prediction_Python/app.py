from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)  # Enabled CORS for frontend fetch support

# Loading our training data
model = pickle.load(open("boston_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        feature_order = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
                         "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]
        features = [data.get(f, 0.0) for f in feature_order]
        prediction = model.predict([features])[0]
        return jsonify({"prediction": round(prediction * 1000, 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)