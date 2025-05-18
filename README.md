# 🚀 Startup Ecosystem Map（django-backend-api）

A lightweight backend project providing RESTful APIs built with **Django** and **Django REST Framework**, featuring:

- 🌍 A **Startup Ecosystem Map** by industry
- 📈 Real-time **US Stock Quotes API** (e.g., AAPL, MSFT)
- 🐳 Easy deployment with **Docker Compose**
- 📄 Designed for frontend API integration

---

## 📂 Project Structure
├── api/ # API logic
├── demo_project/ # Django project settings
├── templates/ # HTML templates (e.g. industry summary)
├── Dockerfile # Docker build config
├── docker-compose.yml # Docker service definition
├── requirements.txt # Dependencies

---

## 🚀 Quick Start

### 🔧 Local Development
pip install -r requirements.txt
python manage.py runserver
Open in browser:
http://localhost:8000/api/industry_summary/Fintech
http://localhost:8000/api/stocks/quotes

### 🐳 Run with Docker (Recommended)
docker-compose up --build

## 🌐 API Endpoints
| Endpoint                           | Method | Description                           |
| ---------------------------------- | ------ | ------------------------------------- |
| `/api/list/selectAll`              | GET    | Retrieve all items from database      |
| `/api/industry_summary/<industry>` | GET    | Industry overview: market & companies |
| `/api/stocks/quotes`               | GET    | Real-time stock market data (US)      |
