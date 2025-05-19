from django.core.management.base import BaseCommand
from django.utils import timezone
from scholarshipapp.models import ScholarshipProgram
from datetime import timedelta

class Command(BaseCommand):
    help = 'Creates sample scholarship programs'

    def handle(self, *args, **kwargs):
        # First, delete existing programs
        ScholarshipProgram.objects.all().delete()

        # Sample programs data
        programs = [
            {
                'title': 'STEM Excellence Scholarship',
                'description': 'For outstanding students pursuing degrees in Science, Technology, Engineering, or Mathematics. This scholarship aims to support future innovators and researchers.',
                'requirements': '''
                - Minimum GPA of 3.5
                - Major in STEM field
                - Research or project experience
                - Two letters of recommendation
                - Personal statement
                ''',
                'amount': 25000,
                'deadline': timezone.now() + timedelta(days=90)
            },
            {
                'title': 'Global Leadership Fellowship',
                'description': 'Supporting future leaders with a demonstrated commitment to international cooperation and cross-cultural understanding.',
                'requirements': '''
                - Strong leadership experience
                - International exposure
                - Community service record
                - Essay on global challenges
                - Two letters of recommendation
                ''',
                'amount': 30000,
                'deadline': timezone.now() + timedelta(days=120)
            },
            {
                'title': 'Digital Innovation Award',
                'description': 'For students pursuing studies in Computer Science, AI, Data Science, or related fields with innovative project ideas.',
                'requirements': '''
                - Portfolio of tech projects
                - GitHub repository
                - Innovation proposal
                - Technical assessment
                - Interview
                ''',
                'amount': 20000,
                'deadline': timezone.now() + timedelta(days=60)
            },
            {
                'title': 'Healthcare Heroes Scholarship',
                'description': 'Supporting students in medical, nursing, and healthcare-related programs who show commitment to community health.',
                'requirements': '''
                - Healthcare major
                - Volunteer experience
                - Essay on healthcare vision
                - Academic excellence
                - Reference from healthcare professional
                ''',
                'amount': 35000,
                'deadline': timezone.now() + timedelta(days=150)
            },
            {
                'title': 'Creative Arts Grant',
                'description': 'For talented students in visual arts, music, theater, or other creative fields who demonstrate exceptional artistic ability.',
                'requirements': '''
                - Portfolio submission
                - Artist statement
                - Performance record
                - Creative project proposal
                - Interview
                ''',
                'amount': 15000,
                'deadline': timezone.now() + timedelta(days=45)
            },
            {
                'title': 'Environmental Sustainability Fellowship',
                'description': 'Supporting students committed to environmental conservation and sustainable development through research and innovation.',
                'requirements': '''
                - Environmental project proposal
                - Research outline
                - Sustainability impact statement
                - Academic excellence
                - Reference letters
                ''',
                'amount': 22000,
                'deadline': timezone.now() + timedelta(days=75)
            },
            {
                'title': 'Women in Engineering Scholarship',
                'description': 'Empowering female students pursuing engineering degrees with financial support and mentorship opportunities.',
                'requirements': '''
                - Female engineering student
                - Technical project experience
                - Leadership potential
                - Academic merit
                - Career goals statement
                ''',
                'amount': 28000,
                'deadline': timezone.now() + timedelta(days=100)
            },
            {
                'title': 'Social Impact Innovation Grant',
                'description': 'For students developing innovative solutions to social challenges in their communities through technology or social entrepreneurship.',
                'requirements': '''
                - Social impact project plan
                - Community engagement record
                - Innovation description
                - Implementation timeline
                - Budget proposal
                ''',
                'amount': 18000,
                'deadline': timezone.now() + timedelta(days=80)
            },
            {
                'title': 'Future Educators Scholarship',
                'description': 'Supporting aspiring teachers committed to transforming education and making a difference in students\' lives.',
                'requirements': '''
                - Education major
                - Teaching experience/internship
                - Educational philosophy
                - Academic excellence
                - Reference from educator
                ''',
                'amount': 20000,
                'deadline': timezone.now() + timedelta(days=110)
            },
            {
                'title': 'Business Innovation Scholarship',
                'description': 'For entrepreneurial students with innovative business ideas and demonstrated leadership potential.',
                'requirements': '''
                - Business plan
                - Leadership experience
                - Innovation pitch
                - Financial projections
                - Market analysis
                ''',
                'amount': 25000,
                'deadline': timezone.now() + timedelta(days=95)
            }
        ]

        # Create programs
        for program_data in programs:
            program = ScholarshipProgram.objects.create(**program_data)
            self.stdout.write(
                self.style.SUCCESS(f"Created program: {program.title}")
            ) 