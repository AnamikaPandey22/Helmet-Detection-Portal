# 🪖 Helmet Detection Portal using YOLOv8n

> A Flask-based computer vision web application for detecting helmet usage in uploaded images using **YOLOv8n**. The project demonstrates how an object detection model can be integrated into a web application for **traffic safety monitoring and automated helmet compliance detection**.

---

## 📌 Overview

Road safety is a major concern, particularly for two-wheeler riders. Manual monitoring of helmet compliance can be time-consuming and difficult to scale.

The **Helmet Detection Portal** uses a trained **YOLOv8n object detection model** to identify helmet usage in images and display the detection results through a simple Flask-based web interface.

The application allows a user to:

1. Upload an image
2. Run helmet detection using YOLOv8n
3. Generate an annotated image
4. View detected objects with bounding boxes

The project demonstrates the integration of **deep learning, computer vision, and web development** into a practical safety-monitoring application.

---

## 🎯 Objectives

The main objectives of this project are to:

* Detect helmet usage automatically from images
* Apply YOLOv8 object detection to traffic-safety scenarios
* Provide a simple web interface for image-based inference
* Display model predictions using bounding boxes
* Demonstrate deployment of a computer vision model through Flask
* Provide a foundation for future real-time traffic monitoring systems

---

# ✨ Features

* 📤 **Image Upload**
  Upload traffic or rider images directly through the web interface.

* 🪖 **Helmet Detection**
  Detect helmet-related objects using a trained YOLOv8n model.

* 📦 **Bounding Box Visualization**
  Display detected objects with bounding boxes and labels.

* 🌐 **Web-Based Interface**
  Access the detection system through a browser.

* ⚡ **Fast Inference**
  YOLOv8n provides a lightweight architecture suitable for relatively fast inference.

* 🔌 **Flask Backend**
  Flask handles image uploads, model inference, and result rendering.

---

# 🧠 How It Works

The application follows a simple computer vision pipeline:

```text
              ┌──────────────────┐
              │   User Uploads   │
              │      Image       │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │  Flask Backend   │
              │  Receives Image  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   YOLOv8n Model  │
              │    Inference     │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Object Detection │
              │  + Bounding Box  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Annotated Image  │
              └────────┬─────────┘
                       │
                       ▼
              ┌──────────────────┐
              │ Display Results   │
              │   in Web Portal  │
              └──────────────────┘
```

---

# 🔍 Detection Pipeline

The core workflow can be summarized as:

```text
Input Image
     ↓
Image Preprocessing
     ↓
YOLOv8n Inference
     ↓
Object Detection
     ↓
Confidence Filtering
     ↓
Bounding Box Generation
     ↓
Annotated Output
     ↓
Web Interface
```

---

# 🤖 Model

### YOLOv8n

The project uses **YOLOv8n (nano)** from the Ultralytics YOLO family.

YOLO (You Only Look Once) is a real-time object detection architecture that performs object localization and classification in a single inference pipeline.

The **YOLOv8n** variant is designed to be lightweight, making it suitable for applications where inference speed and computational efficiency are important.

### Model File

The trained model is stored as:

```text
models/
└── best.pt
```

`best.pt` contains the trained model weights used for inference.

---

# 🛠️ Tech Stack

| Technology      | Purpose                                     |
| --------------- | ------------------------------------------- |
| **Python**      | Core programming language                   |
| **YOLOv8n**     | Object detection                            |
| **Ultralytics** | YOLO model framework                        |
| **OpenCV**      | Image processing                            |
| **Flask**       | Web application backend                     |
| **HTML/CSS**    | Frontend interface                          |
| **Pytesseract** | OCR integration / text extraction component |

---

# 📁 Project Structure

```text
Helmet-Detection-Portal/
│
├── app.py
│
├── models/
│   └── best.pt
│
├── templates/
│   └── index.html
│
├── static/
│   └── uploads/
│
├── requirements.txt
│
└── README.md
```

### File Description

| File / Directory       | Purpose                               |
| ---------------------- | ------------------------------------- |
| `app.py`               | Flask application and inference logic |
| `models/best.pt`       | Trained YOLOv8n model                 |
| `templates/index.html` | Web interface                         |
| `static/uploads/`      | Uploaded and processed images         |
| `requirements.txt`     | Python dependencies                   |
| `README.md`            | Project documentation                 |

---

# 🚀 Getting Started

## Prerequisites

Make sure the following are installed:

* Python 3.9+
* pip
* Git

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Helmet-Detection-Portal.git

cd Helmet-Detection-Portal
```

> Replace `your-username` with the actual GitHub username or repository URL.

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the Application

```bash
python app.py
```

The Flask development server should start locally.

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🖥️ Using the Portal

Once the application is running:

### Step 1 — Open the Portal

Navigate to:

```text
http://127.0.0.1:5000
```

### Step 2 — Upload an Image

Select an image containing one or more two-wheeler riders.

### Step 3 — Run Detection

The Flask backend sends the image to the YOLOv8n model for inference.

### Step 4 — View Results

The processed image is returned with detected objects highlighted using bounding boxes and labels.

Example workflow:

```text
Original Image
      ↓
Upload
      ↓
YOLOv8n
      ↓
Detection
      ↓
Annotated Image
```

---

# 📊 Example Output

A typical output may contain detections such as:

```text
Detection Results

Helmet
Confidence: 0.91

No Helmet
Confidence: 0.87
```

The exact labels and confidence values depend on the classes used during model training.

---

# 🔬 Computer Vision Workflow

The application combines several components:

### 1. Image Acquisition

The user provides an image through the Flask web interface.

### 2. Image Processing

OpenCV is used to read and process the uploaded image.

### 3. Object Detection

YOLOv8n analyzes the image and predicts:

* Object class
* Bounding-box coordinates
* Detection confidence

### 4. Result Visualization

The detected objects are drawn on the original image.

### 5. Web Rendering

The annotated image is returned to the browser through the Flask application.

---

# 🧩 Role of Pytesseract

**Pytesseract** can be used as an OCR component for extracting text from images.

In a broader traffic-monitoring system, OCR can potentially be used for applications such as:

```text
Traffic Image
     ↓
YOLO Detection
     ↓
Identify Vehicle
     ↓
Number Plate Region
     ↓
OCR
     ↓
Extract Plate Text
```

However, the primary focus of this repository is the **helmet detection module**.

---

# 👥 Project Contribution

This repository represents my contribution to the **helmet detection component** of a collaborative computer-vision project.

### My contribution

* YOLOv8-based helmet detection
* Model inference integration
* Flask-based detection workflow
* Image upload and result handling
* Bounding-box visualization

Other project components, including **OCR and analytics**, were developed by other team members.

This separation is documented to clearly distinguish the scope of my contribution within the collaborative project.

---

# 🌍 Potential Applications

The system can serve as a foundation for:

### 🚦 Traffic Safety Monitoring

Automatically monitor helmet compliance among two-wheeler riders.

### 📹 CCTV Analysis

Extend the system to process traffic surveillance footage.

### 🛣️ Smart Traffic Systems

Integrate helmet detection into intelligent transportation systems.

### 📸 Automated Violation Detection

Combine helmet detection with number-plate recognition to identify potential violations.

### 🏙️ Smart City Applications

Use computer vision for automated traffic-rule monitoring.

---

# ⚠️ Limitations

The current implementation is primarily designed for **image-based detection**.

Potential limitations include:

* Performance depends on image quality
* Poor lighting can affect detection
* Occlusion may reduce detection accuracy
* Small or distant riders can be difficult to detect
* Model performance depends on the quality and diversity of training data
* Image-based inference is not equivalent to a complete real-time traffic surveillance system

---

# 🔮 Future Enhancements

Several improvements can extend the current system.

### 🎥 1. Video-Based Detection

Process video streams instead of individual images.

```text
Video
  ↓
Frame Extraction
  ↓
YOLOv8
  ↓
Helmet Detection
  ↓
Annotated Video
```

### 🔢 2. Number Plate Recognition

Integrate OCR and license-plate detection to associate helmet violations with vehicle numbers.

### ⚡ 3. Real-Time Detection

Deploy the model on live CCTV or camera feeds.

### ☁️ 4. Cloud Deployment

Deploy the Flask application using a cloud platform for remote access.

### 📊 5. Analytics Dashboard

Add statistics such as:

* Total riders detected
* Helmet compliance percentage
* Violations detected
* Detection trends over time

### 📱 6. Mobile Integration

Provide an API that can be consumed by a mobile or traffic-monitoring application.

### 🚀 7. Model Optimization

Explore techniques such as:

* Quantization
* Model pruning
* ONNX export
* GPU acceleration

for improved inference performance.

---

# 📈 Possible Evaluation Metrics

For evaluating the object detection model, useful metrics include:

| Metric             | Purpose                                            |
| ------------------ | -------------------------------------------------- |
| **Precision**      | Measures how many predicted detections are correct |
| **Recall**         | Measures how many relevant objects are detected    |
| **mAP@50**         | Mean Average Precision at IoU 0.50                 |
| **mAP@50–95**      | Average precision across multiple IoU thresholds   |
| **Inference Time** | Measures prediction speed                          |

These metrics can be reported after evaluating the trained model on a held-out test/validation dataset.

---

# 🔐 Responsible Use

Helmet detection technology should be treated as an **assistive computer-vision system**, not as an infallible enforcement mechanism.

Real-world deployment should account for:

* False detections
* Poor visibility
* Camera placement
* Privacy considerations
* Model bias
* Human verification where appropriate

---

# 📚 Technologies & Resources

This project builds upon open-source tools and frameworks including:

* Ultralytics YOLO
* PyTorch
* OpenCV
* Flask
* Pytesseract

---

# 👩‍💻 Author

### Anamika Pandey

**BCA | AI/ML | Computer Vision**

Areas of interest:

* Artificial Intelligence
* Machine Learning
* Computer Vision
* Deep Learning
* Generative AI
* Data Structures & Algorithms

---

# 📜 License

This project is intended primarily for **academic and educational purposes**.

The trained model, datasets, and third-party libraries may be subject to their respective licenses and terms of use.

---

# 🙌 Acknowledgements

Special thanks to the open-source communities behind:

* **Ultralytics**
* **YOLO**
* **PyTorch**
* **OpenCV**
* **Flask**
* **Tesseract OCR**

---

## ⭐ Project Highlights

```text
🪖 Helmet Detection
🤖 YOLOv8n
👁️ Computer Vision
🌐 Flask Web Application
📦 Object Detection
📸 Image Processing
🔍 OCR Integration
🚦 Traffic Safety
```

> Built as an academic computer-vision project exploring the integration of **YOLOv8 object detection with a Flask-based web application**.
