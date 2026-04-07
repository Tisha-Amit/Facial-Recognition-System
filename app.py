from flask import Flask, request, jsonify, render_template
import cv2
import numpy as np
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

name_mapping = {
    1: "Tisha Amit",
    2: "Priyanshi Vasa",
    3: "Om Ahir",
    4: "Nidhi Tak"
}

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Hostel Visitors Log").sheet1

latest_result = {"name": "Unknown", "timestamp": "", "verified": False}

@app.route('/recognize', methods=['POST'])
def recognize_face():
    # Get image from ESP32
    global latest_result
    data = request.get_data()
    nparr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        roi_gray = gray[y:y+h, x:x+w]
        id, confidence = recognizer.predict(roi_gray)
        print(f"\n[RECOGNIZED] ID={id} | Confidence={confidence:.1f}")

        name = name_mapping.get(id, f"User {id}")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        verified = confidence < 50

        if verified:
            sheet.append_row([id, name, confidence, timestamp])
            print(f"[LOGGED] {name} → Google Sheet")
        else:
            print(f"[REJECTED] {name} (Confidence too high)")

        latest_result = {"name": name, "timestamp": timestamp, "verified": verified}
        return jsonify({"status": "Success", "id": id, "confidence": confidence, "name": name})
    
    print("")
    return jsonify({"status": "error", "message": "No face detected"})

@app.route('/recognize_status')
def recognize_status():
    global latest_result
    return jsonify(latest_result)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Match port in serverUrl