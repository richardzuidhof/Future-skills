from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from the Backend Application!"

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify(status="ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)