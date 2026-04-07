import cv2
import os
import numpy as np
from PIL import Image

# Path to folder with photos
path = r'C:\Users\Tisha\OneDrive\Desktop\Web camera IoT\faces'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    faceSamples = []
    ids = []
    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')  # Grayscale
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(imagePath)[-1].split('.')[0].replace('user', ''))  # e.g., user1.jpg -> 1
        faces = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces:
            faceSamples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)
    return faceSamples, ids

# Create 'faces' folder and add photos (e.g., user1.jpg, user2.jpg)
if not os.path.exists(path):
    os.makedirs(path)
# Move or copy your resized photos here manually

print("Training faces. It will take a few seconds. Wait ...")
faces, ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('trainer.yml')  # Save the trained model
print("Training complete. Model saved as trainer.yml")