from django.db import models
from django.contrib.auth.models import User
from admins.models import Service

# Create your models here.

class Servc(models.Model):
    SERVICE_LOCATION= (
        ('Kathmandu','Kathmandu'),
        ('Bhaktapur','Bhaktapur'),
        ('Lalitpur','Lalitpur')
    )

    service_user = models.ForeignKey(User, max_length=100, null=True, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Service,max_length=100, null=True, on_delete=models.CASCADE)
    service_location = models.CharField(max_length=100,choices=SERVICE_LOCATION,null=True)

