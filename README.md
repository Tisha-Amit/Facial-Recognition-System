# 📸 IoT-Based Facial Recognition System

## 📌 Overview

This project is an **IoT-based facial recognition system** that captures images using a camera module (ESP32-CAM / webcam), processes them using Python, and identifies individuals using a trained face recognition model.

It can be used for **hostel entry systems, attendance systems, or security applications**.

---

## 🚀 Features

* 📷 Real-time image capture
* 🧠 Face detection and recognition
* 🗂️ Dataset training using stored face images
* 🔐 Identity verification system
* 🌐 Web-based interface (Flask)
* ☁️ Optional cloud/logging integration

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **Flask**
* **ESP32-CAM / Webcam**
* **Face Recognition (LBPH / Haar Cascade)**

---

## 📁 Project Structure

```
WEB-CAMERA-IOT/
│
├── app.py                  # Main Flask app
├── receive_image.py        # Receives images from camera
├── train_faces.py          # Model training script
├── test_faces.py           # Face recognition testing
├── templates/              # HTML files
├── faces/                  # Dataset (training images)
├── trainer.yml             # Trained model file
├── credentials.json        # API credentials (ignored)
└── .gitignore
```

---

## ⚙️ How It Works

1. Camera captures image (ESP32-CAM / webcam)
2. Image is sent to the Python server
3. Faces are detected using OpenCV
4. Model compares with trained dataset
5. Identity is recognized and processed

---

## ▶️ Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install Dependencies

```
pip install opencv-python flask numpy
```

### 3. Add Dataset

* Place face images inside `faces/`
* Name format: `user1.jpg`, `user2.jpg`, etc.

### 4. Train Model

```
python train_faces.py
```

### 5. Run Application

```
python app.py
```

---

## 🔐 Security Note

* `credentials.json` is excluded for security reasons
* Do not upload sensitive API keys to GitHub

---

## 📌 Applications

* Hostel Visitor Entry System
* Smart Attendance System
* Security & Surveillance
* IoT Automation Projects

---

## 👩‍💻 Author

**Tisha Amit**
B.Tech CSE (3rd Year)

---

## ⭐ Future Improvements

* Face recognition using deep learning (CNN)
* Cloud database integration
* Mobile app interface
* Real-time alerts & notifications
