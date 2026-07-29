# Helmet Detection Portal using YOLOv8n and Pytesseract

A Flask-based computer vision web application for detecting helmet usage in images using a YOLOv8n model. This project focuses on traffic safety monitoring and demonstrates real-time inference through a simple web interface.

---

## Features - 

- Image upload through a web portal

- Helmet detection using YOLOv8

- Annotated output with bounding boxes

- Flask-based backend for inference

---

## Tech Stack -

- Python

- YOLOv8n (Ultralytics)

- OpenCV

- Flask

---

## Project Structure -

Helmet-Detection-Portal/
├── app.py
├── models/
│ └── best.pt
├── templates/
│ └── index.html
├── static/
│ └── uploads/
├── requirements.txt
└── README.md


---

## How to Run -

1. Clone the repository:
```bash
git clone https://github.com/your-username/Helmet-Detection-Portal.git
```
Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

Open browser and go to:

http://127.0.0.1:5000

Note on Contribution

This repository contains my contribution to the helmet detection module of a collaborative project. Other components such as OCR and analytics were handled by different team members.

Future Enhancements -

1. Video-based helmet detection

2. Integration with number plate recognition

3. Deployment on cloud platforms

