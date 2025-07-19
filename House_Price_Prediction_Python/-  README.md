# 🏡 Boston House Price Predictor

A web-based machine learning application that predicts housing prices in Boston based on user inputs for 13 key features. Built with Flask (Python), styled frontend, and a trained regression model. Supports real-time input validation and instant predictions.

---

## 📌 Project Overview

This project combines a regression-based ML model with a responsive web frontend to create an interactive experience where users can estimate Boston house prices based on location, crime rate, tax rate, and more.

**Tech Stack:**
- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Backend:** Flask (Python), Pickle, scikit-learn
- **Integration:** JSON API, Flask-CORS
- **Model:** Pre-trained linear regression model on Boston housing dataset

---

## 🔧 Features

| Layer        | Functionality                                     |
|--------------|---------------------------------------------------|
| 🌐 Frontend   | Responsive form UI with tooltip guidance         |
| ✅ Validation | Inline field-level error messages                |
| ⚙️ Backend    | JSON prediction endpoint using Flask              |
| 🤖 Model      | Pre-trained scikit-learn regression model         |
| ⚡ Live UI    | Real-time predictions rendered instantly         |

---

## 🧠 How It Works

### 1. User Inputs:
Users enter values for these 13 features:
CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT

### 2. Frontend Validates:
JavaScript checks each field:
- Required
- Numeric

### 3. Data Sent to Backend:
On each keystroke (debounced), data is sent to `/predict` via `fetch()` as JSON.

### 4. Backend Processes:
Flask receives the data, ensures correct feature order, feeds it to the model, and returns the prediction.

### 5. Prediction Displayed:
Result is shown beneath the form in real-time.

---


---

## 🚀 Run Locally

1. Clone repo
2. Install dependencies:
   ```bash
   pip install flask flask-cors scikit-learn numpy
3. Make sure boston_model.pkl is present
4. Run
    python app.py
5. Visit: http://127.0.0.1:5000

## 📈 Future Enhancements- Deploy on Render or Railway
- Add sliders for continuous features
- Log predictions to database
- Dark mode toggle
- Mobile-responsive layout


## 🙋 Developer Jeevarathinam V
Bachelor of Technology in AI & Data Science, Chennai
Skills: Python · Flask · ML · Frontend · Full-stack · Model Deployment

