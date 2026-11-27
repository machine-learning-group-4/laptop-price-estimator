# Used Laptop Price Estimator

## 1. Project Overview

The Used Laptop Price Estimator is a machine learning project designed to predict the estimated market price of a used laptop based on its specifications and condition.

The application allows users to enter relevant laptop information through a simple frontend interface. The information is sent to a Python Flask backend, which communicates with a trained machine learning model to generate an estimated price.

## 2. Project Objectives

- Develop a machine learning model capable of estimating used laptop prices.
- Explore and preprocess a suitable laptop pricing dataset.
- Train and evaluate the machine learning model.
- Develop a backend API using Flask.
- Build a simple frontend interface for user interaction.
- Integrate the frontend, backend and trained model into one application.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning and model evaluation |
| Joblib | Saving and loading trained models |
| Flask | Backend API development |
| Flask-CORS | Frontend-backend communication |
| HTML, CSS and JavaScript | Frontend development |
| Git and GitHub | Version control and collaboration |
| Jupyter Notebook | Data exploration and model experimentation |

## 4. Project Structure

```text
laptop-price-estimator/
│
├── backend/
│   ├── app.py
│   └── requirements.txt
│
├── dataset/
│   └── (Project datasets)
│
├── frontend/
│   └── (Frontend application files)
│
├── model/
│   └── (Trained machine learning model)
│
├── notebooks/
│   └── (Data exploration and model experiments)
│
├── .gitignore
└── README.md
```

## Possible Structure

```text
used-laptop-price-estimator/
│
├── dataset/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── notebooks/
│   ├── data_cleaning.ipynb
│   ├── eda.ipynb
│   ├── model_training.ipynb
│   └── model_evaluation.ipynb
│
├── model/
│   ├── laptop_price_model.pkl
│   └── preprocessing_pipeline.pkl
│
├── backend/
│   ├── app.py
│   ├── predict.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore
```

The `.venv` virtual environment is maintained locally and excluded from version control.

## 5. Team Distribution of Responsibilities

The project is being developed by a team of six members.

| Member | Responsibility |
|---|---|
| Member 1 | Project coordination and requirements |
| Member 2 | Dataset collection and research |
| Member 3 | Data preprocessing and machine learning |
| Member 4 | Model evaluation and experimentation |
| Member 5 | Frontend development |
| Member 6 | Backend development and API integration |

*Note: The distribution above is a proposed documentation template. Update it to reflect the actual responsibilities agreed upon by the group.*

### Backend Development Responsibilities

The backend is responsible for:

- Developing the Flask application.
- Creating API endpoints.
- Receiving laptop specifications from the frontend.
- Validating incoming user data.
- Loading and communicating with the trained machine learning model.
- Returning predicted prices as JSON responses.
- Handling errors and invalid requests.

## 6. Application Workflow

The application follows this general workflow:

1. The user enters laptop specifications into the frontend.
2. The frontend sends the information to the Flask backend.
3. The backend validates the submitted information.
4. The backend passes the information to the trained machine learning model.
5. The model generates an estimated laptop price.
6. The backend returns the prediction to the frontend.
7. The frontend displays the estimated price to the user.

## 7. Backend Setup

### Prerequisites

- Python installed
- Git installed
- VS Code or another Python-compatible editor

### Clone the repository

```bash
git clone https://github.com/machine-learning-group-4/laptop-price-estimator.git
```

Navigate into the project:

```bash
cd laptop-price-estimator
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install dependencies

```bash
pip install -r backend/requirements.txt
```

### Run the backend

From the project root:

```bash
python backend/app.py
```

The backend will run locally at:

```text
http://127.0.0.1:5000/
```

## 8. API Endpoints

| Endpoint | HTTP Method | Description |
|---|---|---|
| `/` | GET | Checks whether the API is running |
| `/predict` | POST | Receives laptop specifications and returns a price prediction |

The prediction endpoint accepts JSON input. Its final input fields and response format will be determined by the trained model and frontend integration requirements.

## 9. Project Status

**Current development stage:** Initial project setup and backend development.

Planned milestones:

- [x] Create GitHub repository.
- [x] Establish initial project directory structure.
- [x] Set up Python virtual environment.
- [x] Install initial backend dependencies.
- [ ] Explore and prepare the dataset.
- [ ] Train and evaluate the machine learning model.
- [ ] Develop the Flask prediction API.
- [ ] Develop the frontend interface.
- [ ] Integrate the frontend, backend and trained model.
- [ ] Test and document the complete application.

## 10. Contributors

Machine Learning Group 4

GitHub Repository:

https://github.com/machine-learning-group-4/laptop-price-estimator.git

---

**Note:** This project is developed for educational purposes as part of a group machine learning project. Predicted prices are estimates and may differ from actual market prices.