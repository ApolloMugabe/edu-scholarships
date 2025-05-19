import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.files import File
from scholarshipapp.models import University, Testimonial
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Adds sample universities and testimonials'

    def handle(self, *args, **kwargs):
        # Create directories if they don't exist
        for dir_path in [
            os.path.join(settings.MEDIA_ROOT, 'universities'),
            os.path.join(settings.MEDIA_ROOT, 'testimonials'),
            os.path.join(settings.STATIC_ROOT, 'images', 'universities'),
            os.path.join(settings.STATIC_ROOT, 'images', 'testimonials'),
        ]:
            os.makedirs(dir_path, exist_ok=True)

        # Sample universities data
        universities_data = [
            {
                'name': 'Harvard University',
                'description': 'A private Ivy League research university in Cambridge, Massachusetts. Established in 1636, it is the oldest institution of higher learning in the United States.',
                'location': 'Cambridge, Massachusetts, USA',
                'website_url': 'https://www.harvard.edu',
                'image_name': 'harvard.jpg',
                'established_year': 1636,
                'is_featured': True,
                'ranking': 1
            },
            {
                'name': 'Stanford University',
                'description': 'A private research university in Stanford, California. Known for its academic achievements, wealth, and proximity to Silicon Valley.',
                'location': 'Stanford, California, USA',
                'website_url': 'https://www.stanford.edu',
                'image_name': 'stanford.jpg',
                'established_year': 1885,
                'is_featured': True,
                'ranking': 2
            },
            {
                'name': 'Massachusetts Institute of Technology',
                'description': 'A private land-grant research university in Cambridge, Massachusetts. MIT is widely known for its innovation and academic strength.',
                'location': 'Cambridge, Massachusetts, USA',
                'website_url': 'https://www.mit.edu',
                'image_name': 'mit.jpg',
                'established_year': 1861,
                'is_featured': True,
                'ranking': 3
            }
        ]

        # Create universities
        created_universities = {}
        for data in universities_data:
            image_name = data.pop('image_name')
            university = University.objects.create(**data)
            created_universities[university.name] = university

            # Handle university image
            static_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'universities', image_name)
            if os.path.exists(static_image_path):
                media_image_path = os.path.join(settings.MEDIA_ROOT, 'universities', image_name)
                shutil.copy2(static_image_path, media_image_path)
                with open(media_image_path, 'rb') as f:
                    university.image.save(image_name, File(f), save=True)

            self.stdout.write(self.style.SUCCESS(f'Created university: {university.name}'))

        # Sample testimonials data with more entries
        testimonials_data = [
            {
                'name': 'Emily Johnson',
                'role': 'Computer Science Graduate',
                'university': created_universities['Massachusetts Institute of Technology'],
                'content': 'The scholarship enabled me to pursue my dream of studying Computer Science at MIT. I am now working at a leading tech company, developing AI solutions that make a difference.',
                'image_name': 'emily.jpg',
                'is_featured': True
            },
            {
                'name': 'Michael Chen',
                'role': 'Business Administration Student',
                'university': created_universities['Harvard University'],
                'content': 'Thanks to the scholarship, I could focus on my studies at Harvard Business School without financial worries. It opened doors to incredible opportunities in the business world.',
                'image_name': 'michael.jpg',
                'is_featured': True
            },
            {
                'name': 'Sarah Williams',
                'role': 'Engineering Graduate',
                'university': created_universities['Stanford University'],
                'content': "The mentorship and financial support helped me excel in my engineering studies at Stanford. Now I'm leading innovative projects in sustainable energy.",
                'image_name': 'sarah.jpg',
                'is_featured': True
            },
            {
                'name': 'David Martinez',
                'role': 'Physics Researcher',
                'university': created_universities['Massachusetts Institute of Technology'],
                'content': 'The scholarship program not only funded my education but also connected me with brilliant minds in physics. The research opportunities at MIT were incredible.',
                'image_name': 'david.jpg',
                'is_featured': False
            },
            {
                'name': 'Lisa Zhang',
                'role': 'Medical Student',
                'university': created_universities['Harvard University'],
                'content': 'Being a scholarship recipient at Harvard Medical School has been life-changing. The support system and resources available are exceptional.',
                'image_name': 'lisa.jpg',
                'is_featured': False
            },
            {
                'name': 'James Wilson',
                'role': 'Data Science Graduate',
                'university': created_universities['Stanford University'],
                'content': "Stanford's data science program, combined with the scholarship support, prepared me perfectly for my career in AI and machine learning.",
                'image_name': 'james.jpg',
                'is_featured': True
            },
            {
                'name': 'Maria Rodriguez',
                'role': 'Environmental Science Student',
                'university': created_universities['Harvard University'],
                'content': 'The scholarship allowed me to focus on environmental research and sustainability projects. Harvard\'s resources are unmatched.',
                'image_name': 'maria.jpg',
                'is_featured': False
            },
            {
                'name': 'Alex Thompson',
                'role': 'Robotics Engineer',
                'university': created_universities['Massachusetts Institute of Technology'],
                'content': "MIT's robotics program and the scholarship support helped me turn my passion for automation into groundbreaking research.",
                'image_name': 'alex.jpg',
                'is_featured': True
            }
        ]

        # Create testimonials
        for data in testimonials_data:
            image_name = data.pop('image_name')
            testimonial = Testimonial.objects.create(**data)

            # Handle testimonial image
            static_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'testimonials', image_name)
            if os.path.exists(static_image_path):
                media_image_path = os.path.join(settings.MEDIA_ROOT, 'testimonials', image_name)
                shutil.copy2(static_image_path, media_image_path)
                with open(media_image_path, 'rb') as f:
                    testimonial.image.save(image_name, File(f), save=True)

            self.stdout.write(self.style.SUCCESS(f'Created testimonial for: {testimonial.name}')) 