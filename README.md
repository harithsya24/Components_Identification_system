# ⚡ ElectroCom-61: Electronics Component Detection

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![YOLOv5](https://img.shields.io/badge/Model-YOLOv5s-red?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> End-to-end object detection pipeline to identify **61 types of electronic components** from images — with automated CI/CD, Docker containerization, and a REST API for serving predictions.

---

## 📌 Overview

**ElectroCom-61** is a production-ready MLOps project built on **YOLOv5s** that detects electronics parts like resistors, capacitors, sensors, Arduino boards, and more — directly from images.

The project covers the complete lifecycle:

```
Data Ingestion → Preprocessing → Training → Evaluation → API Serving → Docker → CI/CD
```

**Use cases:**
- ✅ PCB assembly verification
- ✅ Electronics inventory management
- ✅ Automated quality inspection
- ✅ Hobby & educational projects

---

## 🏗️ Project Architecture

```
ElectroCom-61/
│
├── Components_Data/               # Dataset
│   ├── train/images & labels/
│   ├── valid/images & labels/
│   ├── test/images & labels/
│   └── data.yaml
│
├── src/
│   ├── data_ingestion.py          # Download & organize dataset
│   ├── preprocessing.py           # Augmentation & validation
│   ├── train.py                   # Model training pipeline
│   ├── evaluate.py                # Metrics & model validation
│   └── predict.py                 # Inference helper
│
├── app/
│   ├── app.py                     # Flask / FastAPI app
│   ├── templates/                 # (if Flask UI)
│   └── static/
│
├── yolov5/                        # YOLOv5 submodule
│
├── runs/
│   ├── train/exp/weights/         # Saved model weights
│   └── detect/exp/                # Detection outputs
│
├── Dockerfile                     # Container definition
├── docker-compose.yml             # Multi-service orchestration
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # GitHub Actions pipeline
└── README.md
```

---

## 🗂️ Dataset

**61 classes** including: batteries, LEDs, resistors, capacitors, inductors, transistors, Arduino boards, Raspberry Pi, sensors, relays, switches, and more.

| Split | Path |
|-------|------|
| Train | `Components_Data/train/` |
| Validation | `Components_Data/valid/` |
| Test | `Components_Data/test/` |
| Config | `Components_Data/data.yaml` |

---

## 🔁 End-to-End Pipeline

### 1️⃣ Data Ingestion & Preprocessing

```bash
python src/data_ingestion.py     # Download & organize raw dataset
python src/preprocessing.py      # Validate annotations, augment if needed
```

- Validates image-label pairs
- Checks class distribution
- Applies augmentation (flips, mosaic, HSV shifts via YOLOv5 config)

---

### 2️⃣ Model Training

```bash
python yolov5/train.py \
    --img 640 \
    --batch 8 \
    --epochs 25 \
    --data Components_Data/data.yaml \
    --weights yolov5s.pt \
    --project runs/train \
    --name exp
```

| Argument | Value | Description |
|----------|-------|-------------|
| `--img` | `640` | Input image resolution |
| `--batch` | `8` | Batch size |
| `--epochs` | `25` | Training epochs |
| `--weights` | `yolov5s.pt` | Pretrained YOLOv5 small backbone |

> ✅ Best weights saved to `runs/train/exp/weights/best.pt`

---

### 3️⃣ Model Evaluation

```bash
python src/evaluate.py \
    --weights runs/train/exp/weights/best.pt \
    --data Components_Data/data.yaml \
    --img 640
```

Outputs:
- mAP@0.5 and mAP@0.5:0.95
- Precision / Recall per class
- Confusion matrix
- F1-Confidence curve

---

### 4️⃣ API Serving (Flask / FastAPI)

```bash
cd app/
python app.py
```

The API exposes a `/predict` endpoint:

```http
POST /predict
Content-Type: multipart/form-data

file: <image>
```

**Sample Response:**
```json
{
  "detections": [
    { "class": "resistor", "confidence": 0.91, "bbox": [120, 45, 200, 110] },
    { "class": "capacitor", "confidence": 0.87, "bbox": [300, 60, 380, 140] }
  ],
  "total_detected": 2
}
```

---

## 🐳 Docker — Containerization

### Build & Run Locally

```bash
# Build the image
docker build -t electrocom61:latest .

# Run the container
docker run -p 5000:5000 electrocom61:latest
```

### Using Docker Compose

```bash
docker-compose up --build
```

**Dockerfile overview:**
```dockerfile
FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app/app.py"]
```

> 🌐 API will be available at `http://localhost:5000`

---

## ⚙️ CI/CD — GitHub Actions

Every push to `main` automatically triggers the full pipeline:

```
Push to main
    │
    ├── ✅ Lint & Code Quality (flake8)
    ├── ✅ Unit Tests (pytest)
    ├── ✅ Docker Image Build
    ├── ✅ Model Evaluation Check (mAP threshold gate)
    └── ✅ Deploy Container Locally / Push to Registry
```

**`.github/workflows/ci-cd.yml` highlights:**

```yaml
name: ElectroCom61 CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Run Tests
        run: pytest tests/

      - name: Build Docker Image
        run: docker build -t electrocom61:latest .

      - name: Run Container (smoke test)
        run: |
          docker run -d -p 5000:5000 electrocom61:latest
          sleep 5
          curl -f http://localhost:5000/health
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/your-username/ElectroCom-61.git
cd ElectroCom-61

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run data ingestion
python src/data_ingestion.py

# 4. Train the model
python yolov5/train.py --img 640 --batch 8 --epochs 25 \
    --data Components_Data/data.yaml --weights yolov5s.pt

# 5. Start the API
python app/app.py

# OR use Docker
docker-compose up --build
```

---

## 📊 Model Summary

| Property | Value |
|----------|-------|
| Architecture | YOLOv5s |
| Classes | 61 |
| Input Size | 640 × 640 |
| Batch Size | 8 |
| Epochs | 25 |
| Serving | Flask / FastAPI |
| Container | Docker |
| CI/CD | GitHub Actions |

---

## 📄 License

- **Dataset:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code:** [MIT License](https://opensource.org/licenses/MIT)

---

## 🙌 Acknowledgements

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
- Electronics dataset contributors
