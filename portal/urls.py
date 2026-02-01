from django.urls import path
from . import views

urlpatterns = [
    # The main dashboard for the New Hire
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # The trigger for the automated IT request
    path('request-it/', views.check_and_request_it_access, name='request_it'),
    # Registration
    path('register/', views.register_view, name='register'),
    # Sign NDA
    path('sign-nda/', views.sign_nda, name='sign_nda'),
    # Complete security training
    path('complete-training/', views.complete_security_training, name='complete_training'),
]