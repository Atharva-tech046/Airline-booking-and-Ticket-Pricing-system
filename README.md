# Airline-booking-and-Ticket-Pricing-system
# ✈️ SkyLink: Airline Booking & Dynamic Pricing System

**A full-stack flight reservation system featuring real-time dynamic pricing logic, visual seat selection, and ACID-compliant transactional integrity.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-orange)

## 📖 Project Overview
SkyLink is not just a standard booking application; it is a simulation of real-world airline engineering challenges. Moving beyond simple data storage, this project implements **business logic at the database layer** to ensure data integrity and profitability.

The core differentiator is the **Dynamic Pricing Engine**, which automatically adjusts ticket costs based on demand windows (e.g., a booking made 2 days before departure costs 1.5x more than one made 30 days in advance), without manual intervention.

### 🚀 Key Features
* **💸 Dynamic Pricing Engine:** A Python-based algorithm that calculates ticket prices in real-time based on the gap between *Booking Date* and *Departure Date*.
* **💺 Visual Seat Mapping:** An interactive frontend grid (HTML/CSS/JS) allowing users to select specific seats (e.g., 12A, 12B) rather than just a generic ticket.
* **🔒 Concurrency Handling:** Uses `select_for_update` (Row-Level Locking) to prevent double-booking of the same seat by simultaneous users.
* **🗄️ Normalized Schema:** Optimized PostgreSQL schema with `OneToOne` constraints to enforce strictly unique seat assignments.

---

## 🛠️ Technical Architecture

### Tech Stack
* **Backend:** Django 5.0 (Python)
* **Database:** PostgreSQL (Production-grade RDBMS)
* **Frontend:** Django Templates, HTML5, CSS Grid (for Seat Map)
* **ORM:** Django ORM with complex aggregation and filtering

### Database Schema
The system relies on 5 core relational models:
1.  **`Airport`**: Lookup table for origin/destination codes (e.g., JFK, LHR).
2.  **`Flight`**: The central entity connecting two airports and a time slot.
3.  **`PricingRule`**: Configuration table storing the logic (e.g., *0-7 days = 1.5x multiplier*).
4.  **`Seat`**: Represents individual inventory. Uses composite keys to ensure (Flight + Row + Letter) is unique.
5.  **`Booking`**: Links a `User` to a `Seat`. Uses a `OneToOne` relationship to physically block a seat once sold.

---
### Prerequisites
* Python 3.x
* PostgreSQL installed locally


## ⚙️ Installation & Setup
```bash
python -m venv venv
```

# Windows
```bash
venv\Scripts\activate
```
# Mac/Linux
```bash
source venv/bin/activate
```
### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/airline-booking-system.git](https://github.com/YOUR_USERNAME/airline-booking-system.git)
cd airline-booking-system


