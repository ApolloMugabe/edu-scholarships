# edu-scholarships
take home exam for django

# EduScholarships

A comprehensive scholarship management platform built with Django and Bootstrap, designed to connect students with educational opportunities and donors.

## Features

- **For Students**
  - Secure user authentication and profile management
  - Browse and search available scholarship programs
  - Apply for scholarships with document upload
  - Real-time application status tracking
  - Application history and notifications

- **For Donors**
  - Secure donor registration and profile management
  - View and filter student applications
  - Secure payment integration for donations
  - Donation history and tax receipts
  - Analytics dashboard

- **For Administrators**
  - Advanced admin dashboard
  - Application review and processing
  - User management and moderation
  - Financial reporting and analytics
  - Email notification system

## Tech Stack

- **Backend**: Django 5.0
- **Frontend**: Bootstrap 5, JavaScript
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Authentication**: Django AllAuth
- **File Storage**: AWS S3 (Production)
- **Deployment**: GitHub Actions, Heroku/Railway
- **Email**: SendGrid
- **Monitoring**: Sentry

## Prerequisites

- Python 3.8+
- PostgreSQL (for production)
- Git
- AWS Account (for S3 storage)
- Virtual environment (recommended)

## Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/eduscholarships.git
   cd eduscholarships
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   Create a `.env` file in the project root:
   ```env
   # Django
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1

   # Database
   DATABASE_URL=sqlite:///db.sqlite3

   # Email
   EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
   DEFAULT_FROM_EMAIL=noreply@eduscholarships.com

   # AWS (for production)
   AWS_ACCESS_KEY_ID=your-access-key
   AWS_SECRET_ACCESS_KEY=your-secret-key
   AWS_STORAGE_BUCKET_NAME=your-bucket-name
   AWS_S3_REGION_NAME=your-region
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

## Deployment

### GitHub Actions Setup

1. Fork this repository
2. Enable GitHub Actions in your repository
3. Add the following secrets to your repository:
   - `DJANGO_SECRET_KEY`
   - `DATABASE_URL`
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `AWS_STORAGE_BUCKET_NAME`
   - `EMAIL_HOST_USER`
   - `EMAIL_HOST_PASSWORD`

### Deployment Options

#### Heroku Deployment
1. Create a Heroku account
2. Install Heroku CLI
3. Login to Heroku:
   ```bash
   heroku login
   ```
4. Create Heroku app:
   ```bash
   heroku create your-app-name
   ```
5. Add PostgreSQL addon:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```
6. Configure environment variables:
   ```bash
   heroku config:set DJANGO_SECRET_KEY=your-secret-key
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=your-app-name.herokuapp.com
   ```
7. Deploy:
   ```bash
   git push heroku main
   ```

#### Railway Deployment
1. Create a Railway account
2. Connect your GitHub repository
3. Add environment variables in Railway dashboard
4. Deploy through Railway dashboard

## Project Structure

```
eduscholarships/
├── scholarshipapp/          # Main application
│   ├── models/             # Database models
│   ├── views/              # View functions
│   ├── forms/              # Forms
│   ├── urls/               # URL patterns
│   ├── templates/          # HTML templates
│   ├── static/            # Static files
│   └── tests/             # Test cases
├── eduscholarships/        # Project settings
│   ├── settings/          # Settings modules
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── static/                # Project static files
├── media/                 # User-uploaded files
├── templates/            # Base templates
├── manage.py             # Django management script
├── requirements/         # Split requirements
│   ├── base.txt         # Base requirements
│   ├── dev.txt          # Development requirements
│   └── prod.txt         # Production requirements
├── .github/             # GitHub Actions workflows
├── .gitignore           # Git ignore file
└── README.md            # Project documentation
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Security

- All passwords are hashed using Django's built-in password hashers
- CSRF protection enabled
- XSS protection through Django's template system
- SQL injection protection through Django ORM
- File upload validation and scanning
- Rate limiting on authentication endpoints

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support:
- Create an issue in the repository
- Email: support@eduscholarships.com
- Documentation: [docs.eduscholarships.com](https://docs.eduscholarships.com)

## Acknowledgments

- Django Documentation
- Bootstrap Team
- All contributors and maintainers