# Marcelo Salinas - Portfolio Website

A professional portfolio website built with Django.

## Setup Instructions

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the development server:
   ```
   python manage.py runserver
   ```
4. Visit http://127.0.0.1:8000/ in your browser to view the portfolio

## Customization

- Edit `templates/index.html` to update content
- Modify `static/style.css` to change styling

## Deployment

For production deployment:

1. Set `DEBUG = False` in `portfolio/settings.py`
2. Update `ALLOWED_HOSTS` with your domain
3. Generate a new secure `SECRET_KEY`
4. Collect static files:
   ```
   python manage.py collectstatic
   ```
5. Deploy to your preferred hosting service 