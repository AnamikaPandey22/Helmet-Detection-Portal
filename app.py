# app.py

import os
from flask import Flask, render_template, request, jsonify
from ultralytics import YOLO
from PIL import Image
import io
import cv2
import numpy as np
import pytesseract

def detect_number_plate_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 170, 200)

    cnts, _ = cv2.findContours(
        edged.copy(),
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            plate_roi = gray[y:y+h, x:x+w]

            text = pytesseract.image_to_string(
                plate_roi, config="--psm 7"
            )
            return text.strip()

    return None


app = Flask(__name__)

# Load the YOLOv8 model file
model_path = r'C:\Users\anami\OneDrive\Desktop\Projects\Helmet_Detection_App\models\best(2).pt'

# The YOLOv8 syntax to load a custom model
try:
    model = YOLO(model_path)
except Exception as e:
    raise FileNotFoundError(f"Failed to load model from {model_path}. Error: {e}")

# Set up the upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_helmet():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        try:
            # Read the image from the request
            img = Image.open(io.BytesIO(file.read())).convert('RGB')

            # Run inference
            results = model(img)

            # Get the annotated image (YOLOv8 returns a list of result objects)
            # The `plot()` method draws bounding boxes on the image
            annotated_img = results[0].plot()

            # Convert the annotated image to a format for web display
            img_bgr = cv2.cvtColor(annotated_img, cv2.COLOR_RGB2BGR)
            _, img_encoded = cv2.imencode('.png', img_bgr)

            return img_encoded.tobytes()

        except Exception as e:
            return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)