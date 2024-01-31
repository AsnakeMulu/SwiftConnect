from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Request(models.Model):
    your_choices = (
        ('pending', u'pending'),
        ('active', u'active'),
        ('rejected', u'rejected'),
    )

    sender_BIC = models.CharField(max_length=255)
    sender_name = models.CharField(max_length=50)
    receiver_BIC = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=50)
    request_description = models.CharField(max_length=1050)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=32, choices=your_choices, null=True, blank=True)
    created_date = models.DateTimeField(max_length=255)