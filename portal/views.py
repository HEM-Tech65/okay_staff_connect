from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import EmployeeProfile, ITRequest
from django.shortcuts import render, get_object_or_404
from .models import EmployeeProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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