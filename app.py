from flask import Flask, jsonify, request
from preProcessing import preProcess
from predictionCNN import predict

import os
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Pussy!"


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
      #  class_id, class_name = predict(preprocessed_image_result)
        emotion, prob, rest = predict(output_image_path)
        return jsonify({'emotion_predicted': emotion, 'probability': prob, 'other_emotions': rest})
      #  return jsonify({'class_id': class_id, 'class_name': class_name})
    else:
        return jsonify({'message': preprocessed_image_result})