from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/',methods=['Post','Get'])
def index():
    return jsonify(hello="world")

if __name__ == "__main__":
    app.run(threaded=True, port=5000)
