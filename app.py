from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python API is running!"

@app.route("/run-script", methods=["POST"])
def run_script():
    try:
        data = request.get_json()
        name = data.get("name", "Guest")
        
        # Example: Your Python logic
        result = f"Hello, {name}! Your script ran successfully."

        return jsonify({"status": "success", "result": result}), 200

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Needed to run in Render (Gunicorn handles app object directly)
if __name__ == "__main__":
    app.run(debug=True)
