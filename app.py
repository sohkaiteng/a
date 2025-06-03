from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Python API is running!"

@app.route("/run-script", methods=["POST"])
def run_script():
    try:
        data = request.get_json()
        name = data.get("name", "Guest")
        result = f"Hello, {name}! Your script ran successfully."
        return jsonify({"status": "success", "result": result}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
