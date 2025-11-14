# CoachKat - Personal Training Website

A modern, responsive personal training web application built with Flask and vanilla JavaScript.

## 🛠️ Technologies

- **Front-end**: HTML, Tailwind CSS, JavaScript
- **Back-end**: Flask (Python)
- **Database**: SQLite
- **API**: Google Maps Embed

## Structure

```
ProjectJW_Phase2_Submission/
├── backend/
│   ├── app.py
│   ├── db_init.py
│   ├── schema.sql
│   └── Requirements.txt
├── static/
│   ├── css/styles.css
│   ├── images/
│   ├── js/script.js
│   └── videos/
├── templates/
│   └── index.html
└── coachkat.db
```

## Features

- Video library with database storage
- Contact form with validation
- Light/dark theme switcher
- Responsive design
- Google Maps integration

## Setup

```bash
git clone https://github.com/ray87375/ProjectJW_Phase2_Submission.git
cd ProjectJW_Phase2_Submission
pip install -r backend/Requirements.txt
python backend/db_init.py
python backend/app.py
```

## 📡 API Endpoints

- `GET /` - Main page
- `GET /api/videos` - Fetch videos
- `POST /api/contact` - Submit contact form

## 📊 Database

**videos**: id, title, url, durationSeconds, published_at  
**messages**: id, name, email, message, created_at

## Author

Ray - [GitHub](https://github.com/ray87375)

