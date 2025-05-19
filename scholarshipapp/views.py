from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout
from django.contrib import messages
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *

def is_admin(user):
    return user.is_staff

def is_donor(user):
    return hasattr(user, 'donor')

def is_sponsorship_manager(user):
    return hasattr(user, 'sponsorshipmanager')

def is_admin_or_manager(user):
    return user.is_staff or hasattr(user, 'sponsorshipmanager')

def home(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')[:3]
    programs = ScholarshipProgram.objects.all().order_by('-created_at')[:3]
    universities = University.objects.all()
    return render(request, 'scholarshipapp/home.html', {
        'testimonials': testimonials,
        'programs': programs,
        'universities': universities
    })

def about(request):
    return render(request, 'scholarshipapp/about.html')

def testimonials(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'scholarshipapp/testimonials.html', {'testimonials': testimonials})

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Student.objects.create(
                user=user,
                phone_number=form.cleaned_data['phone_number'],
                address=form.cleaned_data['address'],
                date_of_birth=form.cleaned_data['date_of_birth']
            )
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'scholarshipapp/register.html', {'form': form, 'user_type': 'Student'})

def donor_register(request):
    if request.method == 'POST':
        form = DonorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Donor.objects.create(
                user=user,
                organization=form.cleaned_data['organization'],
                phone_number=form.cleaned_data['phone_number']
            )
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = DonorRegistrationForm()
    return render(request, 'scholarshipapp/register.html', {'form': form, 'user_type': 'Donor'})

@login_required
def scholarship_programs(request):
    programs = ScholarshipProgram.objects.all().order_by('-created_at')
    return render(request, 'scholarshipapp/programs.html', {'programs': programs})

@login_required
def apply_scholarship(request, program_id):
    program = get_object_or_404(ScholarshipProgram, id=program_id)
    if request.method == 'POST':
        form = ScholarshipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.student = request.user.student
            application.program = program
            application.save()
            messages.success(request, 'Application submitted successfully!')
            return redirect('my_applications')
    else:
        form = ScholarshipApplicationForm()
    return render(request, 'scholarshipapp/apply.html', {'form': form, 'program': program})

@login_required
def my_applications(request):
    applications = ScholarshipApplication.objects.filter(student=request.user.student)
    pending_count = applications.filter(status='pending').count()
    approved_count = applications.filter(status='approved').count()
    
    context = {
        'applications': applications,
        'total_count': applications.count(),
        'pending_count': pending_count,
        'approved_count': approved_count,
    }
    return render(request, 'scholarshipapp/my_applications.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'scholarshipapp/contact.html', {'form': form})

@user_passes_test(is_admin)
def admin_dashboard(request):
    applications = ScholarshipApplication.objects.all().order_by('-application_date')
    messages = ContactMessage.objects.filter(is_replied=False).order_by('-created_at')
    donations = Donation.objects.all().order_by('-donation_date')
    return render(request, 'scholarshipapp/admin_dashboard.html', {
        'applications': applications,
        'messages': messages,
        'donations': donations
    })

@user_passes_test(is_admin)
def admin_reply_message(request, message_id):
    message = get_object_or_404(ContactMessage, id=message_id)
    if request.method == 'POST':
        form = AdminReplyForm(request.POST, instance=message)
        if form.is_valid():
            message = form.save(commit=False)
            message.is_replied = True
            message.replied_at = timezone.now()
            message.save()
            messages.success(request, 'Reply sent successfully!')
            return redirect('admin_dashboard')
    else:
        form = AdminReplyForm(instance=message)
    return render(request, 'scholarshipapp/reply_message.html', {'form': form, 'message': message})

@user_passes_test(is_donor)
def donor_dashboard(request):
    applications = ScholarshipApplication.objects.filter(status='pending')
    my_donations = Donation.objects.filter(donor=request.user.donor)
    return render(request, 'scholarshipapp/donor_dashboard.html', {
        'applications': applications,
        'donations': my_donations
    })

@user_passes_test(is_donor)
def make_donation(request, program_id):
    program = get_object_or_404(ScholarshipProgram, id=program_id)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donor = request.user.donor
            donation.program = program
            donation.save()
            messages.success(request, 'Donation made successfully!')
            return redirect('donor_dashboard')
    else:
        form = DonationForm()
    return render(request, 'scholarshipapp/make_donation.html', {'form': form, 'program': program})

@csrf_protect
def custom_logout(request):
    """Custom logout view that handles both GET and POST requests"""
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

@user_passes_test(is_admin_or_manager)
def manager_dashboard(request):
    applications = ScholarshipApplication.objects.all().order_by('-application_date')
    messages = ContactMessage.objects.filter(is_replied=False).order_by('-created_at')
    testimonials = Testimonial.objects.all().order_by('-created_at')
    return render(request, 'scholarshipapp/manager_dashboard.html', {
        'applications': applications,
        'messages': messages,
        'testimonials': testimonials
    })

@user_passes_test(is_admin_or_manager)
def view_application(request, application_id):
    application = get_object_or_404(ScholarshipApplication, id=application_id)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['pending', 'approved', 'rejected']:
            application.status = status
            application.save()
            messages.success(request, f'Application status updated to {status}')
    return render(request, 'scholarshipapp/view_application.html', {'application': application})

def universities(request):
    featured_universities = University.objects.filter(is_featured=True).order_by('ranking')
    all_universities = University.objects.all().order_by('name')
    return render(request, 'scholarshipapp/universities.html', {
        'featured_universities': featured_universities,
        'universities': all_universities
    }) 