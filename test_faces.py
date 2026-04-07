import cv2
import numpy as np
import os

# Load the trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

# Load the face detector
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect and recognize faces
def detect_and_recognize(image_path):
    # Read the test image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = detector.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        # Region of interest
        roi_gray = gray[y:y+h, x:x+w]
        # Recognize the face
        id, confidence = recognizer.predict(roi_gray)
        # Confidence: 0-100, lower is better; typically < 50 is a match
        if confidence < 50:
            name = f"User {id}"  # Map ID to name (e.g., User 1 for user1.jpg)
            print(f"Match found! ID: {id}, Name: {name}, Confidence: {confidence:.2f}%")
        else:
            print(f"No match or low confidence. ID: {id}, Confidence: {confidence:.2f}%")

# Test with a new photo
test_image = '20251013231846.jpg'  # Replace with your test image path
detect_and_recognize(test_image)