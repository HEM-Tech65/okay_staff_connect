from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib import messages
from .models import EmployeeProfile, ITRequest

# Create your views here.

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create EmployeeProfile for the new user
            EmployeeProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'portal/register.html', {'form': form})

@login_required
def sign_nda(request):
    employee = get_object_or_404(EmployeeProfile, user=request.user)
    if not employee.signed_nda:
        employee.signed_nda = True
        employee.save()
        messages.success(request, 'NDA signed successfully!')
    else:
        messages.info(request, 'NDA already signed.')
    return redirect('dashboard')

@login_required
def complete_security_training(request):
    employee = get_object_or_404(EmployeeProfile, user=request.user)
    if not employee.completed_security_training:
        employee.completed_security_training = True
        employee.save()
        messages.success(request, 'Security training completed successfully!')
    else:
        messages.info(request, 'Security training already completed.')
    return redirect('dashboard')

@login_required
def check_and_request_it_access(request):
    employee = get_object_or_404(EmployeeProfile, user=request.user)
    
    # Logic to ensure mandatory tasks are complete [cite: 351]
    if employee.signed_nda and employee.completed_security_training:
        if not employee.it_request_sent:
            ITRequest.objects.create(
                employee=employee,
                status='Pending'
            )
            employee.it_request_sent = True
            employee.save()
            return render(request, 'portal/success.html', {'message': 'IT Request Sent!'})
    
    return render(request, 'portal/error.html', {'message': 'Compliance tasks pending.'})

@login_required
def dashboard_view(request):
    # This fetches the specific staff member's profile from the Data Tier
    profile = get_object_or_404(EmployeeProfile, user=request.user)
    return render(request, 'portal/dashboard.html', {'profile': profile})