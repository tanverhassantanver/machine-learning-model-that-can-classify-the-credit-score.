from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("credit_score_model.pkl")
feature_names = joblib.load("feature_names.pkl")
score_map = joblib.load("score_map.pkl")


@app.route("/")
def home():
    return jsonify({
        "message": "Credit Score Prediction API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        input_data = pd.DataFrame([data])

        missing = [
            col for col in feature_names
            if col not in input_data.columns
        ]

        if missing:
            return jsonify({
                "error": "Missing features",
                "missing_features": missing
            }), 400

        input_data = input_data[feature_names]

        prediction = model.predict(input_data)

        prediction = int(
            np.asarray(prediction).ravel()[0]
        )

        probability = model.predict_proba(input_data)

        confidence = float(probability.max())

        return jsonify({
            "credit_score": score_map[prediction],
            "confidence": round(
                confidence * 100, 2
            )
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)