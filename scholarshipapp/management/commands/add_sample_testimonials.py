import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from scholarshipapp.models import Testimonial
from django.core.files import File

class Command(BaseCommand):
    help = 'Adds sample testimonials with images'

    def handle(self, *args, **kwargs):
        # Create media/testimonials directory if it doesn't exist
        testimonials_dir = os.path.join(settings.MEDIA_ROOT, 'testimonials')
        os.makedirs(testimonials_dir, exist_ok=True)

        # Sample testimonials data
        testimonials_data = [
            {
                'name': 'Emily Johnson',
                'role': 'STEM Scholarship Recipient 2024',
                'content': 'The scholarship enabled me to pursue my dream of studying Computer Science at MIT. I am now working at a leading tech company, developing AI solutions that make a difference.',
                'image_name': 'emily.jpg'
            },
            {
                'name': 'Michael Chen',
                'role': 'Arts Excellence Scholar 2023',
                'content': 'Thanks to the scholarship, I could focus on my artistic development at Parsons School of Design without financial worries. It opened doors to incredible opportunities in the creative industry.',
                'image_name': 'michael.jpg'
            },
            {
                'name': 'Sarah Williams',
                'role': 'Leadership Program Scholar 2024',
                'content': 'The mentorship and financial support helped me develop my leadership skills at Harvard Business School. Now I'm leading initiatives that empower other young entrepreneurs.',
                'image_name': 'sarah.jpg'
            }
        ]

        # First, delete existing testimonials
        Testimonial.objects.all().delete()

        # Create new testimonials
        for data in testimonials_data:
            # Create a new testimonial
            testimonial = Testimonial(
                name=data['name'],
                role=data['role'],
                content=data['content']
            )
            
            # Copy sample image from static to media
            static_image_path = os.path.join(settings.STATIC_ROOT, 'images', 'testimonials', data['image_name'])
            media_image_path = os.path.join(settings.MEDIA_ROOT, 'testimonials', data['image_name'])
            
            # Save the testimonial first
            testimonial.save()
            
            # Try to copy the image if it exists
            if os.path.exists(static_image_path):
                shutil.copy2(static_image_path, media_image_path)
                with open(media_image_path, 'rb') as f:
                    testimonial.image.save(data['image_name'], File(f), save=True)
            
            self.stdout.write(self.style.SUCCESS(f'Created testimonial for {data["name"]}'))) 