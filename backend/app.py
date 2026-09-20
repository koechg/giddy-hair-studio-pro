from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

bookings = []

@app.route("/")
def home():
    return jsonify({
        "message": "Giddy Hair Studio Pro API 💇‍♀️",
        "status": "running",
        "endpoints": ["/api/services", "/api/book", "/api/bookings"]
    })

@app.route("/api/services")
def services():
    return jsonify([
        {"id":1, "name":"Braids & Cornrows", "price":2500, "time":"2-3 hrs"},
        {"id":2, "name":"Silk Press & Cut", "price":3000, "time":"1.5 hrs"},
        {"id":3, "name":"Color & Treatment", "price":4500, "time":"2 hrs"},
        {"id":4, "name":"Locs Retwist", "price":2000, "time":"1 hr"},
    ])

@app.route("/api/book", methods=["POST"])
def book():
    data = request.json
    data["id"] = len(bookings) + 1
    data["created_at"] = datetime.now().isoformat()
    bookings.append(data)
    return jsonify({"success": True, "booking": data}), 201

@app.route("/api/bookings")
def get_bookings():
    return jsonify(bookings)

if __name__ == "__main__":
    app.run(debug=True, port=5000)