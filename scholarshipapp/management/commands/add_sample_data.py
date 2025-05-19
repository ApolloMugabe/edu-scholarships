from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from scholarshipapp.models import *
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Adds sample data to the database'

    def handle(self, *args, **kwargs):
        # Create sponsorship manager
        manager_user = User.objects.create_user(
            username='manager',
            password='manager123',
            first_name='John',
            last_name='Smith',
            email='manager@eduscholarships.com'
        )
        SponsorshipManager.objects.create(
            user=manager_user,
            department='Scholarship Review',
            phone_number='555-0123'
        )
        self.stdout.write(self.style.SUCCESS('Created sponsorship manager'))

        # Create sample applications
        programs = ScholarshipProgram.objects.all()
        students = Student.objects.all()
        
        statuses = ['pending', 'approved', 'rejected']
        for i in range(10):
            student = random.choice(students)
            program = random.choice(programs)
            application_date = timezone.now() - timedelta(days=random.randint(1, 30))
            
            ScholarshipApplication.objects.create(
                student=student,
                program=program,
                status=random.choice(statuses),
                application_date=application_date,
                motivation_letter=f"I am very interested in {program.title} because it aligns with my academic goals..."
            )
        self.stdout.write(self.style.SUCCESS('Created 10 sample applications'))

        # Create testimonials with required images
        testimonials_data = [
            {
                'name': 'Emily Johnson',
                'role': 'STEM Scholarship Recipient 2024',
                'content': 'The scholarship enabled me to pursue my dream of studying Computer Science at MIT. I am now working at a leading tech company, developing AI solutions that make a difference.',
                'image': 'testimonials/emily.jpg'
            },
            {
                'name': 'Michael Chen',
                'role': 'Arts Excellence Scholar 2023',
                'content': 'Thanks to the scholarship, I could focus on my artistic development at Parsons School of Design without financial worries. It opened doors to incredible opportunities in the creative industry.',
                'image': 'testimonials/michael.jpg'
            },
            {
                'name': 'Sarah Williams',
                'role': 'Leadership Program Scholar 2024',
                'content': 'The mentorship and financial support helped me develop my leadership skills at Harvard Business School. Now I'm leading initiatives that empower other young entrepreneurs.',
                'image': 'testimonials/sarah.jpg'
            }
        ]

        for data in testimonials_data:
            Testimonial.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Created 3 testimonials'))

        # Create prestigious universities
        universities_data = [
            {
                'name': 'Massachusetts Institute of Technology',
                'description': 'A world-renowned institution known for its cutting-edge research and innovation in science, technology, and engineering.',
                'image': 'universities/mit.jpg',
                'website_url': 'https://www.mit.edu',
                'location': 'Cambridge, Massachusetts',
                'established_year': 1861
            },
            {
                'name': 'Stanford University',
                'description': 'Leading research university that cultivates innovation and entrepreneurial spirit in the heart of Silicon Valley.',
                'image': 'universities/stanford.jpg',
                'website_url': 'https://www.stanford.edu',
                'location': 'Stanford, California',
                'established_year': 1885
            },
            {
                'name': 'Harvard University',
                'description': 'America's oldest institution of higher learning, known for excellence in education, research, and global leadership.',
                'image': 'universities/harvard.jpg',
                'website_url': 'https://www.harvard.edu',
                'location': 'Cambridge, Massachusetts',
                'established_year': 1636
            }
        ]

        for data in universities_data:
            University.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Created 3 prestigious universities')) 