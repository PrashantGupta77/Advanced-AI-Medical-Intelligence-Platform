# 🏥 Advanced AI Medical Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)
![AI](https://img.shields.io/badge/AI-Medical%20Intelligence-purple)

An end-to-end **AI-powered medical imaging intelligence platform** that analyzes chest X-ray images, predicts pneumonia using Deep Learning, explains model decisions using **Explainable AI (Grad-CAM)**, and generates AI-assisted medical reports using Large Language Models.

The platform provides a complete production-style AI application with:

- 🧠 Deep Learning based disease prediction
- 🔍 Explainable AI using Grad-CAM
- 🤖 LLM-powered medical report generation
- ⚡ FastAPI REST APIs
- 🗄️ Prediction history database
- 🎨 Interactive Streamlit dashboard
- 🐳 Docker-based deployment


---

# 📌 Project Overview

Medical image diagnosis requires not only accurate prediction but also interpretability.

This project builds an AI medical assistant capable of analyzing chest X-ray images and providing:

1. Disease prediction
2. Confidence score
3. Visual explanation of model attention
4. AI-generated medical report
5. Prediction history tracking


The system follows a complete AI pipeline:

```
Chest X-Ray Image
        |
        |
        v
Image Preprocessing
        |
        |
        v
EfficientNetB0 Deep Learning Model
        |
        |
        +----------------+
        |                |
        v                v
 Prediction        Grad-CAM Explanation
        |
        |
        v
LLM Medical Report Generation
        |
        |
        v
Database Storage
```


---

# 🚀 Features


## 🧠 Deep Learning Disease Prediction

The platform uses a trained **EfficientNetB0 Transfer Learning model** for chest X-ray classification.

Supported classes:

```
NORMAL
PNEUMONIA
```


The model provides:

- Disease prediction
- Confidence score
- Real-time inference


---

## 🔍 Explainable AI (Grad-CAM)

Deep learning models are often considered black boxes.

To improve transparency, this project integrates **Grad-CAM (Gradient-weighted Class Activation Mapping)**.


Grad-CAM highlights important regions of the X-ray image that influenced the model prediction.


Pipeline:

```
X-Ray Image

      |

EfficientNetB0

      |

Prediction

      |

Grad-CAM Heatmap

      |

Visual Explanation
```


Benefits:

- Model interpretability
- Visualization of important regions
- Explainable medical AI


---

## 🤖 AI Medical Report Generation

The platform integrates an LLM-based report generation module.

The generated report contains:


```
Findings

Impression

Recommendation
```


Example:

```
Findings:
The chest X-ray shows abnormal opacity
suggestive of infection.

Impression:
Possible pneumonia detected.

Recommendation:
Clinical correlation and further evaluation
are advised.
```


---

# 🏗️ System Architecture


```
                    User
                      |
                      |
                      v

              Streamlit Dashboard
                  Frontend

                      |
                      |
                      v

                 FastAPI Backend

        --------------------------------

        |              |               |

        v              v               v

 EfficientNet     Grad-CAM        LLM Service

  Model             XAI           Report Generator


        |

        |

        v

   SQLite Database

 Prediction History

```


---

# 🛠️ Technology Stack


## Backend

| Technology | Purpose |
|------------|---------|
| Python 3.11 | Programming Language |
| FastAPI | REST API Framework |
| TensorFlow/Keras | Deep Learning |
| EfficientNetB0 | Image Classification |
| SQLAlchemy | Database ORM |
| SQLite | Prediction Storage |
| Pydantic | Configuration Management |


---

## Computer Vision & Explainability

| Technology | Purpose |
|------------|---------|
| Grad-CAM | Explainable AI |
| OpenCV | Image Processing |
| PIL | Image Handling |
| NumPy | Numerical Operations |


---

## Frontend

| Technology | Purpose |
|------------|---------|
| Streamlit | Interactive Dashboard |
| Requests | API Communication |
| Pandas | Data Visualization |


---

## Deployment

| Technology | Purpose |
|------------|---------|
| Docker | Containerization |
| Docker Compose | Multi-container Deployment |


---

# 📂 Project Structure


```
Advanced-AI-Medical-Intelligence-Platform/

│
├── backend/
│
│   ├── app/
│   │
│   │   ├── main.py
│   │   ├── config.py
│   │
│   │   ├── api/
│   │   │   ├── prediction.py
│   │   │   ├── report.py
│   │   │   └── history.py
│   │
│   │   ├── services/
│   │   │   ├── model_service.py
│   │   │   ├── gradcam_service.py
│   │   │   └── llm_service.py
│   │
│   │   ├── database/
│   │   │   ├── database.py
│   │   │   └── models.py
│   │
│   │   └── utils/
│   │
│   ├── models/
│   │   └── final_medical_ai_model.keras
│   │
│   ├── outputs/
│   │   └── gradcam images
│   │
│   ├── uploads/
│   │
│   ├── medical_predictions.db
│   │
│   ├── requirements.txt
│   │
│   └── Dockerfile
│
│
├── frontend/
│
│   ├── streamlit_app.py
│   │
│   ├── requirements.txt
│   │
│   └── Dockerfile
│
│
├── notebooks/

│   ├── 01_data_preparation.ipynb
│   ├── 02_model_training.ipynb
│   ├── 03_model_evaluation.ipynb
│   ├── 04_gradcam.ipynb
│   └── 05_inference.ipynb
│
│
├── results/
│
│   ├── confusion_matrix.png
│   ├── training_accuracy.png
│   ├── training_loss.png
│   └── gradcam_example.png
│
│
├── reports/
│   └── project_report.pdf
│
│
├── docker-compose.yml
│
├── README.md
│
└── .gitignore

```


---

# 🔌 API Documentation


## Health Check


### Endpoint

```
GET /health
```


Response:


```json
{
  "status": "running"
}
```


---

# 🩻 Prediction API


### Endpoint


```
POST /predict/
```


Request:

```
multipart/form-data

file:
    chest_xray.jpeg
```


Response:


```json
{
  "success": true,
  "message": "Prediction completed successfully.",
  "data": {

    "filename": "xray.jpeg",

    "prediction": "PNEUMONIA",

    "confidence": 97.68,

    "model": "EfficientNetB0",

    "gradcam_image": "outputs/gradcam.jpeg"

  }
}
```


---

# 📄 Medical Report API


### Endpoint


```
POST /report/
```


Request:


```json
{
    "prediction":"PNEUMONIA",
    "confidence":97.68
}
```


Response:


```json
{
    "success":true,
    "medical_report":"AI generated medical report"
}
```


---

# 📊 Prediction History API


### Endpoint


```
GET /history/
```


Example Response:


```json
[
    {
        "id":1,
        "filename":"xray.jpeg",
        "prediction":"NORMAL",
        "confidence":84.57,
        "model":"EfficientNetB0",
        "created_at":"2026-07-25"
    }
]
```


---

# 🐳 Docker Deployment


## Build Docker Containers


```bash
docker compose build
```


## Start Application


```bash
docker compose up
```


Application:


Frontend:

```
http://localhost:8501
```


Backend:

```
http://localhost:8000
```


Swagger Documentation:

```
http://localhost:8000/docs
```


---

# 💻 Local Development


## Backend Setup


Navigate:


```bash
cd backend
```


Create environment:


```bash
python -m venv venv
```


Activate:


Windows:

```bash
venv\Scripts\activate
```


Install dependencies:


```bash
pip install -r requirements.txt
```


Run:


```bash
uvicorn app.main:app --reload
```


---

## Frontend Setup


Navigate:


```bash
cd frontend
```


Install dependencies:


```bash
pip install -r requirements.txt
```


Run:


```bash
streamlit run streamlit_app.py
```


---

# 📈 Model Performance


Model:

```
EfficientNetB0 Transfer Learning
```


Input Size:

```
224 x 224
```


Performance:


| Metric | Score |
|--------|-------|
| Accuracy | ~87% |
| AUC | ~0.94 |
| Loss | ~0.30 |


---

# 🔬 Machine Learning Pipeline


```
Dataset

   |

Data Cleaning

   |

Image Preprocessing

   |

Data Augmentation

   |

EfficientNetB0 Training

   |

Evaluation

   |

Grad-CAM Generation

   |

API Deployment

   |

Production Application

```


---

# 🔮 Future Improvements


- Multi-disease classification
- DICOM image support
- Patient authentication
- Cloud deployment
- Medical image segmentation
- Doctor dashboard
- Model monitoring
- MLOps pipeline


---

# ⚠️ Disclaimer


This project is developed for educational and research purposes only.

The predictions generated by this system should not be considered a replacement for professional medical diagnosis.


---

# 👨‍💻 Author


## Prashant Kumar Gupta


AI/ML Engineer


Technical Interests:

- Deep Learning
- Generative AI
- Large Language Models
- Computer Vision
- FastAPI
- MLOps


---

⭐ If you find this project useful, consider giving it a star.