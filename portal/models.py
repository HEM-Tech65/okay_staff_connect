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

    @property
    def progress(self):
        steps = [self.signed_nda, self.completed_security_training, self.it_request_sent]
        completed = sum(steps)
        return completed / 3  # 0, 0.333, 0.666, 1

class ITRequest(models.Model):
    employee = models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=100, default='New Hire Provisioning')
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)