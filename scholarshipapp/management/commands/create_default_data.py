from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from scholarshipapp.models import ScholarshipProgram, Student, ScholarshipApplication
from datetime import timedelta
import random

class Command(BaseCommand):
    help = 'Creates default scholarship programs and sample applications'

    def handle(self, *args, **kwargs):
        # Create default programs
        programs = [
            {
                'title': 'STEM Excellence Scholarship',
                'description': 'For outstanding students in Science, Technology, Engineering, and Mathematics.',
                'requirements': '- Minimum GPA of 3.5\n- Major in STEM field\n- Strong academic record\n- Leadership experience',
                'amount': 10000,
                'deadline': timezone.now() + timedelta(days=90)
            },
            {
                'title': 'Future Leaders Grant',
                'description': 'Supporting students who demonstrate exceptional leadership potential.',
                'requirements': '- Active involvement in student organizations\n- Leadership roles\n- Community service experience\n- Good academic standing',
                'amount': 7500,
                'deadline': timezone.now() + timedelta(days=60)
            },
            {
                'title': 'Global Diversity Scholarship',
                'description': 'Promoting diversity and international understanding in higher education.',
                'requirements': '- International student status\n- Cultural exchange participation\n- Academic excellence\n- English proficiency',
                'amount': 15000,
                'deadline': timezone.now() + timedelta(days=120)
            },
            {
                'title': 'Arts and Humanities Fellowship',
                'description': 'Supporting creative minds in arts, literature, and humanities.',
                'requirements': '- Portfolio submission\n- Creative achievements\n- Academic merit\n- Statement of artistic goals',
                'amount': 8000,
                'deadline': timezone.now() + timedelta(days=45)
            },
            {
                'title': 'Community Service Award',
                'description': 'Recognizing students dedicated to community service and social impact.',
                'requirements': '- Minimum 100 hours of community service\n- Leadership in service projects\n- Letters of recommendation\n- Essay on social impact',
                'amount': 5000,
                'deadline': timezone.now() + timedelta(days=75)
            },
            {
                'title': 'Environmental Sustainability Grant',
                'description': 'Supporting students committed to environmental conservation and sustainability.',
                'requirements': '- Environmental project participation\n- Research in sustainability\n- Academic excellence\n- Commitment to eco-friendly initiatives',
                'amount': 12000,
                'deadline': timezone.now() + timedelta(days=100)
            },
            {
                'title': 'First-Generation Student Scholarship',
                'description': 'Supporting first-generation college students in their academic journey.',
                'requirements': '- First-generation college student\n- Financial need\n- Academic potential\n- Personal statement',
                'amount': 20000,
                'deadline': timezone.now() + timedelta(days=150)
            },
            {
                'title': 'Healthcare Heroes Fund',
                'description': 'Supporting future healthcare professionals and medical researchers.',
                'requirements': '- Healthcare/Medical major\n- Clinical experience\n- Research participation\n- Strong academic record',
                'amount': 25000,
                'deadline': timezone.now() + timedelta(days=180)
            },
            {
                'title': 'Digital Innovation Award',
                'description': 'For students pushing boundaries in technology and digital innovation.',
                'requirements': '- Technology-related projects\n- Innovation portfolio\n- Technical skills\n- Vision statement',
                'amount': 15000,
                'deadline': timezone.now() + timedelta(days=90)
            },
            {
                'title': 'Women in Leadership Scholarship',
                'description': 'Empowering female students to pursue leadership roles.',
                'requirements': '- Leadership potential\n- Academic excellence\n- Community involvement\n- Essay on women in leadership',
                'amount': 18000,
                'deadline': timezone.now() + timedelta(days=120)
            }
        ]

        for program_data in programs:
            ScholarshipProgram.objects.get_or_create(
                title=program_data['title'],
                defaults=program_data
            )

        # Create sample students and applications
        sample_students = [
            {
                'username': 'sarah.johnson',
                'first_name': 'Sarah',
                'last_name': 'Johnson',
                'email': 'sarah.j@example.com',
                'password': 'testpass123'
            },
            {
                'username': 'michael.zhang',
                'first_name': 'Michael',
                'last_name': 'Zhang',
                'email': 'michael.z@example.com',
                'password': 'testpass123'
            },
            {
                'username': 'emma.patel',
                'first_name': 'Emma',
                'last_name': 'Patel',
                'email': 'emma.p@example.com',
                'password': 'testpass123'
            }
        ]

        for student_data in sample_students:
            user, created = User.objects.get_or_create(
                username=student_data['username'],
                defaults={
                    'first_name': student_data['first_name'],
                    'last_name': student_data['last_name'],
                    'email': student_data['email']
                }
            )
            if created:
                user.set_password(student_data['password'])
                user.save()
                Student.objects.create(
                    user=user,
                    phone_number=f'+1555{random.randint(1000000, 9999999)}',
                    address=f'{random.randint(100, 999)} Example Street, City, State',
                    date_of_birth=timezone.now() - timedelta(days=random.randint(7300, 8030))  # 20-22 years old
                )

        # Create sample applications
        programs = ScholarshipProgram.objects.all()
        students = Student.objects.all()
        statuses = ['pending', 'approved', 'rejected']

        for student in students:
            # Each student applies to 2-4 random programs
            for program in random.sample(list(programs), random.randint(2, 4)):
                ScholarshipApplication.objects.get_or_create(
                    student=student,
                    program=program,
                    defaults={
                        'status': random.choice(statuses),
                        'motivation_letter': f'I am very interested in the {program.title} because it aligns with my academic goals...',
                        'application_date': timezone.now() - timedelta(days=random.randint(1, 30))
                    }
                )

        # Create admin user if it doesn't exist
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'is_staff': True,
                'is_superuser': True,
                'email': 'admin@eduscholarships.com',
                'first_name': 'Admin',
                'last_name': 'User'
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        self.stdout.write(self.style.SUCCESS('Successfully created default data')) 