# EduScholarships

A comprehensive scholarship management platform that connects students with educational opportunities and donors. Built with Django and Bootstrap.

## Features

- **For Students**
  - Register and create student profiles
  - Browse available scholarship programs
  - Apply for scholarships with required documentation
  - Track application status
  - View application history

- **For Donors**
  - Register as a donor
  - View student applications
  - Make donations to specific programs
  - Track donation history

- **For Administrators**
  - Manage scholarship programs
  - Review and process applications
  - Respond to student inquiries
  - Monitor donations and program status

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/eduscholarships.git
   cd eduscholarships
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create environment variables file (.env):
   ```bash
   # Create .env file in the project root
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

5. Apply database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser (admin):
   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` in your web browser

## Project Structure

```
eduscholarships/
├── scholarshipapp/          # Main application
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Forms
│   ├── urls.py            # URL patterns
│   └── templates/         # HTML templates
├── static/                # Static files (CSS, JS, images)
├── media/                 # User-uploaded files
├── templates/            # Base templates
├── manage.py             # Django management script
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Usage

1. **For Students**
   - Register as a student
   - Complete your profile
   - Browse available scholarships
   - Apply with required documents
   - Track your applications

2. **For Donors**
   - Register as a donor
   - View student applications
   - Make donations
   - Track your contributions

3. **For Administrators**
   - Access admin panel at `/admin`
   - Manage users and applications
   - Process scholarship applications
   - Monitor donations

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@eduscholarships.com or create an issue in the repository.

## Acknowledgments

-Myself.