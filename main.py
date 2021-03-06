from flask import Flask,request,jsonify
app = Flask(__name__)
import engine as en
from flask_cors import CORS
CORS(app)


@app.route('/api/v1/getAnalysis/', methods=['GET','POST'])
def getMessage():
    # handle the POST request
    content = request.json
    message = content["message"]
    final_result = en.final_analysis(message)
    return jsonify({"data":final_result})



