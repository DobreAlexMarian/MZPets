# MZPets Demo Web App

This repository contains a **minimal Flask MVC demo** for the MZPets web application. The purpose is to showcase a basic project structure with an orange theme, suitable for a quick demonstration.

## Project Structure

```
MZPets/
├─ README.md
├─ src/
│  ├─ app.py            # Flask application entry point
│  ├─ __init__.py
│  ├─ models/           # Simple data models
│  │   ├─ product.py
│  │   └─ category.py
│  ├─ controllers/      # Blueprint‑based controllers
│  │   └─ product_controller.py
│  ├─ templates/        # Jinja2 HTML templates
│  │   ├─ base.html
│  │   └─ index.html
│  └─ static/css/style.css   # Orange‑theme stylesheet
└─ requirements.txt    # Python dependencies
```

## How to Run

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
2. **Start the server**
   ```
   python -m src.app
   ```
3. Open your browser at `http://127.0.0.1:5000/`.

The demo provides a placeholder products page. You can extend the models and controllers as needed.
