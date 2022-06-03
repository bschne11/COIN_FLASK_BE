import os
import cv2
import pandas as pd
import tensorflow as tf
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from imageai.Detection import ObjectDetection
import tensorflow.python.keras



model_path = "./models/resnet50_coco_best_v2.1.0.h5"

basepath = os.path.dirname(__file__)

object_detector = ObjectDetection()
object_detector.setModelTypeAsRetinaNet()
object_detector.setModelPath(model_path)
object_detector.loadModel()
custom_cat = object_detector.CustomObjects(cat=True)

padding = 0.1

def preProcess(imagePath, outputPath):

    detections = object_detector.detectObjectsFromImage(
        input_image=imagePath,
        output_image_path=outputPath,
        minimum_percentage_probability=10,
        custom_objects=custom_cat)

    if detections:  # if cat got detected with enough probability

        # Read image for cropping and delete it afterwards
        image = cv2.imread(imagePath)

        try: 
            os.remove(imagePath)
        except: 
            pass

        height, width, channels = image.shape

        # Get the box around the detected cat
        cat = (sorted(detections, key=lambda cat: cat['percentage_probability'], reverse=True))[0]

        # Retrieve edge coordinates for the detected cat, padding for certainty
        x1 = max(0, int(cat['box_points'][0] * (1 - padding)))
        y1 = max(0, int(cat['box_points'][1] * (1 - padding)))
        x2 = min(width, int(cat['box_points'][2] * (1 + padding)))
        y2 = min(width, int(cat['box_points'][3] * (1 + padding)))

        # Save new cropped cat image
        image = image[y1:y2, x1:x2]

        if image.size:
            cv2.imwrite(outputPath, image,
                        [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            return None
        else:
            return "Empty Image"
    
    else:
        return "No Cat Detected!"