from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/run-script', methods=['POST'])
def run_script():
    data = request.get_json()
    name = data.get("name", "unknown")
    result = f"Hello, {name}. Your data was processed."
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
