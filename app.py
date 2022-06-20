from flask import Flask, jsonify, request
from preProcessing import preProcess
from predictionCNN import predict

import os
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def home():
    return "Hello!"


@app.route('/predictEmotion', methods=['POST'])
def predictEmotion():
  
    # Get the file from the request
    file = request.files['file']

    if file is None:
        return jsonify({'message': "No Image inside the Request"})

    basepath = os.path.dirname(__file__)
    # Store the image to uploads
    sec_filename = secure_filename(file.filename)
    file_path = os.path.join(basepath, 'images', sec_filename)
    file.save(file_path)
    output_image_path = os.path.join(basepath, 'croppedImages', sec_filename)

    # Preprocess the image (crop it)
    preprocessed_image_result = preProcess(file_path, output_image_path)
    # If it is None a cat got detected
    if preprocessed_image_result is None:
        emotion, prob, rest = predict(output_image_path)
        return jsonify({'emotion_predicted': emotion, 'probability': prob, 'other_emotions': rest})
    else:
        return jsonify({'message': preprocessed_image_result})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response