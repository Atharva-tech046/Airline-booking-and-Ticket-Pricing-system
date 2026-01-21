# ✈️ SkyScanner Clone: Airline Reservation System

### A full-stack flight search engine built with Django, featuring dynamic data generation and cloud deployment.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://airline-booking-and-ticket-pricing-system.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

---

## 📖 Overview

This project is a web-based **Airline Reservation System** designed to mimic real-world flight search platforms. Unlike static websites, this application includes a custom **"Data Seeding Engine"** that programmatically fills the database with realistic flight schedules, prices, and routes, allowing for robust testing and demonstration.

The application is fully deployed on **Render** using a CI/CD-like workflow where the database is automatically repopulated upon every deployment.

## ✨ Key Features

* **🔍 Real-Time Search:** Users can filter flights by Origin, Destination, and Travel Date.
* **📊 Dynamic Data Engine:** A custom script (`populate_flights.py`) generates 50+ random flights with realistic pricing algorithms every time the server starts.
* **🎨 Responsive UI:** Professional "Card View" interface with clean CSS styling and interactive elements.
* **☁️ Cloud Deployment:** Hosted on Render with production-grade settings (Gunicorn, WhiteNoise for static files).
* **⚡ Optimized Performance:** Uses SQLite for lightweight, fast queries in the deployment environment.

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **Database:** SQLite (Production compatible with PostgreSQL)
* **Deployment:** Render Cloud, Gunicorn, WhiteNoise

## 🚀 How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Atharva-tech046/airline-portfolio.git](https://github.com/Atharva-tech046/airline-portfolio.git)
    cd airline-portfolio
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Migrate & Seed Database**
    ```bash
    python manage.py migrate
    python populate_flights.py  # <--- The Magic Script!
    ```

5.  **Run Server**
    ```bash
    python manage.py runserver
    ```
    Visit `http://127.0.0.1:8000` in your browser.

## 📂 Project Structure

```text
airline_portfolio/
├── config/              # Django settings & configuration
├── core/                # Main application logic
│   ├── models.py        # Flight & Airport Database Schema
│   ├── views.py         # Search logic & API endpoints
│   └── templates/       # HTML Frontend
├── populate_flights.py  # Custom Data Seeding Script
├── requirements.txt     # Dependency list
└── manage.py            # Django CLI utility
