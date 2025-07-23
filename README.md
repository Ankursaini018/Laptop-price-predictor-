# 💻 Laptop Price Predictor

A machine learning-based web application that predicts laptop prices based on specifications like brand, processor, RAM, storage, and display. Designed for buyers, sellers, and tech enthusiasts who want quick and accurate laptop pricing estimates.

---

## 🌟 Features

* ✅ **Real-time Price Prediction** based on user-selected specifications
* 🧠 **Trained ML Model** using scikit-learn and joblib
* 🌍 **Clean Flask Web Interface** with form inputs and prediction display
* 📊 **Interactive Notebook** for data cleaning, EDA, and model training
* 📖 **Multi-page UI**: Includes Home, About, Contact, Project, and History pages
* ⚙️ **Fully Integrated Pipeline** for categorical encoding & model inference

---

## 📂 Project Structure

├── app.py # Flask application entry point
├── model.joblib # Trained regression model (serialized)
├── laptopPrice.csv # Raw laptop dataset
├── clean\_lptp.csv # Cleaned dataset after preprocessing
├── laptop.ipynb # Jupyter Notebook for EDA & ML training
├── templates/ # HTML templates for UI
│ ├── index.html # Main input form page
│ ├── about.html # About the project or team
│ ├── contact.html # Contact information page
│ ├── project.html # Detailed project explanation
│ ├── history.html # Prediction or usage history display
├── static/ # Static assets (images/icons/CSS)
│ └── \[images and style.css]

