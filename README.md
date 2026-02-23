# ⚡ Electronics Component Detection

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![YOLOv5](https://img.shields.io/badge/Model-YOLOv5s-red?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> End-to-end MLOps pipeline to detect **61 types of electronic components** from images — powered by YOLOv5s, served via Flask, containerized with Docker, and automated through GitHub Actions CI/CD.

---

## 📌 Overview

**ElectroCom-61** detects electronics parts like resistors, capacitors, sensors, Arduino boards, LEDs, and more — directly from images through a Flask web interface.

**Use cases:**
- ✅ PCB assembly verification
- ✅ Electronics inventory management
- ✅ Automated quality inspection
- ✅ Hobby & educational projects

<!-- Add sample detection image here -->
<!-- ![Sample Detection](assets/sample_detection.jpg) -->

---

## 🏗️ Project Structure

```
Components_Identification_system/
├── componentsDetection/       # Core pipeline package (ingestion, training, evaluation)
├── data/                      # Dataset (train / valid / test)
├── artifacts/                 # Model weights & training outputs
├── yolov5/                    # YOLOv5 submodule
├── templates/                 # Flask HTML templates
├── research/                  # Experiments & notebooks
├── validation/                # Validation scripts & results
├── log/                       # Runtime logs
├── app.py                     # Flask web app entry point
├── Dockerfile                 # Container definition
├── requirements.txt           # Dependencies
└── setup.py                   # Package installer
```

---

## 🔁 Pipeline

```
Data Ingestion → Preprocessing → Training → Evaluation → Flask App → Docker → CI/CD
```

| Stage | Description |
|-------|-------------|
| **Data Ingestion** | Downloads and organizes the 61-class dataset |
| **Preprocessing** | Validates annotations and applies augmentation |
| **Training** | Fine-tunes YOLOv5s on the component dataset |
| **Evaluation** | Reports mAP, Precision, Recall, and Confusion Matrix |
| **Flask App** | Serves predictions via a web interface |
| **Docker** | Packages the full app into a portable container |
| **CI/CD** | GitHub Actions auto-builds and tests on every push |

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/Components_Identification_system.git
cd Components_Identification_system

# Install dependencies
pip install -r requirements.txt
python setup.py install

# Run the app
python app.py

# OR with Docker
docker build -t componentsDetection .
docker run -p 8080:8080 componentsDetection
```

---

## 📊 Model

| Property | Value |
|----------|-------|
| Architecture | YOLOv5s |
| Classes | 61 |
| Input Size | 640 × 640 |
| Serving | Flask |
| Container | Docker |
| CI/CD | GitHub Actions |

---

## 📄 License

- **Dataset:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code:** [MIT](./LICENSE)

---

## 🙌 Acknowledgements

- [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5)
