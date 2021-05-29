import json
from flask import *
import text2emotion as te


app = Flask(__name__)

@app.route('/emotion_detector',methods=['GET'])
def index():
    text=request.args.get('text')
    emotionDictionary= te.get_emotion(text)
    return jsonify(emotionDictionary)






if __name__ == "__main__":
    app.run(threaded=True, port=5000)
