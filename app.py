from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python API is running!"

@app.route("/run-script", methods=["POST"])
def run_script():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({"result": f"Hello, {name}!"})
