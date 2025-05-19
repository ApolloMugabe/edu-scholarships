from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('universities/', views.universities, name='universities'),
    path('register/student/', views.student_register, name='student_register'),
    path('register/donor/', views.donor_register, name='donor_register'),
    path('programs/', views.scholarship_programs, name='scholarship_programs'),
    path('apply/<int:program_id>/', views.apply_scholarship, name='apply_scholarship'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('contact/', views.contact, name='contact'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/reply/<int:message_id>/', views.admin_reply_message, name='admin_reply_message'),
    path('donor-dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('make-donation/<int:program_id>/', views.make_donation, name='make_donation'),
    path('manager-dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('application/<int:application_id>/', views.view_application, name='view_application'),
] 