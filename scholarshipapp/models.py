from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organization

class ScholarshipProgram(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    deadline = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ScholarshipApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    program = models.ForeignKey(ScholarshipProgram, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    application_date = models.DateTimeField(auto_now_add=True)
    academic_records = models.FileField(upload_to='academic_records/')
    motivation_letter = models.TextField()

    def __str__(self):
        return f"{self.student.user.username} - {self.program.title}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    university = models.ForeignKey('University', on_delete=models.SET_NULL, null=True, blank=True, related_name='testimonials')
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', help_text="Upload your photo (recommended size: 400x400px)")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-is_featured', '-created_at']

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    website_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='universities/', help_text="Upload university image (recommended size: 800x600px)")
    established_year = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)
    ranking = models.PositiveIntegerField(default=9999, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = 'Universities'
        ordering = ['ranking', 'name']

    def __str__(self):
        return self.name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    reply = models.TextField(null=True, blank=True)
    is_replied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    program = models.ForeignKey(ScholarshipProgram, on_delete=models.CASCADE)
    donation_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.donor.organization} - ${self.amount}"

class SponsorshipManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - Sponsorship Manager" 