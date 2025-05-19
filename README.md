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
- Email: apollomugabe807@gmail.com
- contact. 0762499958

## Acknowledgments

- Django Documentation
- Bootstrap Team
- All contributors and maintainers
