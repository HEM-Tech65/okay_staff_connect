from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class EmployeeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    signed_nda = models.BooleanField(default=False)
    completed_security_training = models.BooleanField(default=False)
    it_request_sent = models.BooleanField(default=False)
    onboarding_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class ITRequest(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100, default='New Hire Provisioning')
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)