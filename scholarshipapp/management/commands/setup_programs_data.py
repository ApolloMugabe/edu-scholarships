from django.core.management.base import BaseCommand
from django.utils import timezone
from scholarshipapp.models import ScholarshipProgram
from decimal import Decimal

class Command(BaseCommand):
    help = 'Adds sample scholarship programs'

    def handle(self, *args, **kwargs):
        # Sample scholarship programs data
        programs_data = [
            {
                'title': 'Global Leadership Excellence Scholarship',
                'description': 'A prestigious scholarship for future global leaders showing exceptional leadership potential and academic excellence.',
                'requirements': '- Minimum GPA of 3.8\n- Leadership roles in extracurricular activities\n- Strong letters of recommendation\n- International exposure preferred',
                'deadline': timezone.now().date() + timezone.timedelta(days=90),
                'amount': Decimal('50000.00')
            },
            {
                'title': 'STEM Innovation Scholarship',
                'description': 'Supporting bright minds in Science, Technology, Engineering, and Mathematics to drive innovation and technological advancement.',
                'requirements': '- Major in STEM field\n- Research experience\n- Minimum GPA of 3.5\n- Innovation project proposal',
                'deadline': timezone.now().date() + timezone.timedelta(days=60),
                'amount': Decimal('35000.00')
            },
            {
                'title': 'Arts and Humanities Fellowship',
                'description': 'Empowering creative minds to pursue excellence in arts, literature, philosophy, and cultural studies.',
                'requirements': '- Portfolio submission\n- Essay on cultural impact\n- Two faculty recommendations\n- Demonstrated artistic achievement',
                'deadline': timezone.now().date() + timezone.timedelta(days=120),
                'amount': Decimal('25000.00')
            },
            {
                'title': 'Future Entrepreneurs Grant',
                'description': 'Supporting aspiring entrepreneurs with innovative business ideas and demonstrated entrepreneurial spirit.',
                'requirements': '- Business plan submission\n- Entrepreneurial experience\n- Market analysis\n- Financial projections',
                'deadline': timezone.now().date() + timezone.timedelta(days=45),
                'amount': Decimal('40000.00')
            },
            {
                'title': 'Environmental Sustainability Scholarship',
                'description': 'For students committed to environmental conservation and sustainable development practices.',
                'requirements': '- Environmental project proposal\n- Volunteer experience\n- Research in sustainability\n- Academic excellence',
                'deadline': timezone.now().date() + timezone.timedelta(days=75),
                'amount': Decimal('30000.00')
            },
            {
                'title': 'Healthcare Heroes Scholarship',
                'description': 'Supporting future medical professionals committed to improving global healthcare.',
                'requirements': '- Pre-med or healthcare-related major\n- Clinical volunteer experience\n- Research participation\n- Strong academic record',
                'deadline': timezone.now().date() + timezone.timedelta(days=100),
                'amount': Decimal('45000.00')
            },
            {
                'title': 'Digital Innovation Award',
                'description': 'For students pushing boundaries in computer science, AI, and digital technologies.',
                'requirements': '- Programming portfolio\n- Tech project demonstration\n- Coding competition participation\n- Innovation statement',
                'deadline': timezone.now().date() + timezone.timedelta(days=80),
                'amount': Decimal('42000.00')
            },
            {
                'title': 'Social Impact Fellowship',
                'description': 'Supporting students dedicated to creating positive social change through innovative solutions.',
                'requirements': '- Social impact project proposal\n- Community service record\n- Leadership experience\n- Change-maker essay',
                'deadline': timezone.now().date() + timezone.timedelta(days=110),
                'amount': Decimal('35000.00')
            },
            {
                'title': 'Women in Leadership Scholarship',
                'description': 'Empowering female leaders to achieve their full potential in their chosen fields.',
                'requirements': '- Leadership roles\n- Mentorship experience\n- Gender equality advocacy\n- Academic excellence',
                'deadline': timezone.now().date() + timezone.timedelta(days=95),
                'amount': Decimal('38000.00')
            },
            {
                'title': 'Global Diversity Grant',
                'description': 'Promoting cultural diversity and international understanding through education.',
                'requirements': '- Cultural exchange experience\n- Language proficiency\n- Cross-cultural project\n- Diversity statement',
                'deadline': timezone.now().date() + timezone.timedelta(days=85),
                'amount': Decimal('32000.00')
            },
            {
                'title': 'Research Excellence Fellowship',
                'description': 'Supporting groundbreaking research across all academic disciplines.',
                'requirements': '- Research proposal\n- Publication record\n- Faculty endorsement\n- Research experience',
                'deadline': timezone.now().date() + timezone.timedelta(days=70),
                'amount': Decimal('48000.00')
            },
            {
                'title': 'Public Service Scholarship',
                'description': 'For students committed to careers in public service and government leadership.',
                'requirements': '- Public service record\n- Policy proposal\n- Government internship\n- Leadership potential',
                'deadline': timezone.now().date() + timezone.timedelta(days=130),
                'amount': Decimal('36000.00')
            },
            {
                'title': 'Creative Writing Grant',
                'description': 'Supporting emerging writers and storytellers in developing their craft.',
                'requirements': '- Writing portfolio\n- Published works\n- Creative writing samples\n- Literary achievements',
                'deadline': timezone.now().date() + timezone.timedelta(days=65),
                'amount': Decimal('28000.00')
            },
            {
                'title': 'Sports Excellence Award',
                'description': 'Supporting student-athletes who excel both in sports and academics.',
                'requirements': '- Athletic achievements\n- Sports leadership\n- Academic performance\n- Coach recommendation',
                'deadline': timezone.now().date() + timezone.timedelta(days=55),
                'amount': Decimal('33000.00')
            },
            {
                'title': 'First-Generation Scholar Program',
                'description': 'Supporting first-generation college students in achieving their educational dreams.',
                'requirements': '- First-generation status\n- Personal statement\n- Community involvement\n- Academic potential',
                'deadline': timezone.now().date() + timezone.timedelta(days=150),
                'amount': Decimal('40000.00')
            }
        ]

        # Create scholarship programs
        for data in programs_data:
            program, created = ScholarshipProgram.objects.get_or_create(
                title=data['title'],
                defaults={
                    'description': data['description'],
                    'requirements': data['requirements'],
                    'deadline': data['deadline'],
                    'amount': data['amount']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created scholarship program: {program.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Scholarship program already exists: {program.title}')) 