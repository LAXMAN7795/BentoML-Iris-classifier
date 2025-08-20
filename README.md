# ​ BentoML Iris Classifier

A lightweight machine learning REST API for classifying Iris species, powered by **BentoML**, **scikit-learn**, and containerized via **Docker**.

---

##  Project Structure

├── .gitignore
├── bentofile.yaml # BentoML configuration for bundling and model serving
├── requirements.txt # Python dependencies
├── train.py # Script to train and save the model
├── service.py # BentoML service definition and serving logic
├── test.py # Test script for sanity-checking the API
└── README.md # (You are here)

---

##  Getting Started

### Prerequisites

- Python 3.8+
- Docker
- (Optional) BentoML CLI: `pip install bentoml`

### 1. Train the Model

Train the Iris classifier and register it in BentoML:

```bash
python train.py
2. Serve Locally with BentoML
Build and serve the model:

bash
Copy
Edit
bentoml build
bentoml serve iris_classifier:latest
Or simply:

bash
Copy
Edit
bentoml serve service.py:svc
3. Test the API
Test with sample input:

bash
Copy
Edit
python test.py
Or use curl:

bash
Copy
Edit
curl -X POST http://localhost:3000/classify \
  -H 'Content-Type: application/json' \
  -d '{"iris_data": [[5.1, 3.5, 1.4, 0.2]]}'
Expected output:

json
Copy
Edit
2
Containerization & Deployment
Once built and tested, containerize and run the service:

bash
Copy
Edit
docker build -t laxman920/iris-classifier:latest .
docker push laxman920/iris-classifier:latest
Run it in detached mode:

bash
Copy
Edit
docker run -d -p 3000:3000 laxman920/iris-classifier:latest
Check logs or status:

bash
Copy
Edit
docker ps
docker logs <container_id>
API Endpoints
GET /healthz — Health check

POST /classify — Classify Iris samples; expects JSON payload:

json
Copy
Edit
{
  "iris_data": [[5.1, 3.5, 1.4, 0.2]]
}
Response example:

json
Copy
Edit
{"prediction": "setosa"}
Swagger/OpenAPI UI available at: http://localhost:3000

Tech Stack
Component	Description
BentoML	Model packaging & serving framework
scikit-learn	ML model implementation
Docker	Containerization for easy deployment
Python	Core implementation language

How to Contribute
Feel free to:

Improve model performance

Add more API endpoints (e.g. batch predict)

Enhance CI/CD or GitHub Actions

Add test coverage

Contributions are welcome via pull requests — thank you!

Author & License
Created and maintained by laxman920.

This project is released under the MIT License.

Quick Reference: Pull & Run
bash
Copy
Edit
docker pull laxman920/iris-classifier:latest
docker run -d -p 3000:3000 laxman920/iris-classifier:latest
curl -X POST http://localhost:3000/classify \
     -H 'Content-Type: application/json' \
     -d '{"iris_data":[[5.1,3.5,1.4,0.2]]}'
