# Django HTMX Demo

A modern Django application demonstrating the power of HTMX and Tailwind CSS.

## Features

- Real-time search with HTMX
- Modern UI with Tailwind CSS
- No JavaScript framework required
- Live CSS reloading
- Django debug toolbar

## Setup

### Using GitHub Codespaces (Recommended for the tutorial)

1. Click the "Code" button on this repository
2. Select "Open with Codespaces"
3. Click "New codespace"

The environment will be automatically configured for you.

### Local Development

#### Prerequisites

- Python 3.8 or higher
- Git
- Node.js 14+ and npm (for Tailwind CSS)
- A code editor (VS Code recommended)

#### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/[your-username]/django-htmx-demo.git
cd django-htmx-demo
```

2. Create a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Tailwind CSS:
```bash
python manage.py tailwind install
```

5. Create a `.env` file:
```bash
cp .env.example .env
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Start the development server:
```bash
# Terminal 1: Django server
python manage.py runserver

# Terminal 2: Tailwind compiler
python manage.py tailwind start
```

Visit http://localhost:8000 to see the application.

## Development

### VS Code Setup

Install recommended extensions:
- Python
- Django
- Tailwind CSS IntelliSense

### File Structure

```
django_htmx_demo/
├── app/                # Main Django project
├── core/              # Main application
├── static/            # Static files
├── templates/         # Template files
└── theme/            # Tailwind theme
```

### Common Commands

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Compile Tailwind CSS
python manage.py tailwind build
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
