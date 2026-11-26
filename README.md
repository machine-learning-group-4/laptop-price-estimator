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

## 5. Team Distribution of Responsibilities

The project is being developed by a team of six members.

| Member | Responsibility |
|---|---|
| Joseph Justus Chukwukaima | Data Collection and Processing |
| Edobor-Osula Gabriel Owen | Exploratory Data Analysis (EDA) |
| Robinson Ibitamuno Asimetamunopiri | Model Development |
| Inifiye-Israel Conquered | Model Evaluation and Optimization |
| Okoye Ogechi Angel | Frontend development |
| Ukah-Nwokejiezi Nzubechukwu Christiantus | Backend development and Model integration |
| Okuneso Harold Oluwamayowa | Project Documentation |

## 6. Application Workflow

The application follows this general workflow:

1. The user enters laptop specifications into the frontend.
2. The frontend sends the information to the Flask backend.
3. The backend validates the submitted information.
4. The backend passes the information to the trained machine learning model.
5. The model generates an estimated laptop price.
6. The backend returns the prediction to the frontend.
7. The frontend displays the estimated price to the user.


## 7. Contributors

1. shychristian
2. Kimi1407

GitHub Repository:

https://github.com/machine-learning-group-4/laptop-price-estimator.git

---

**Note:** This project is developed for educational purposes as part of a group machine learning project. Predicted prices are estimates and may differ from actual market prices.
