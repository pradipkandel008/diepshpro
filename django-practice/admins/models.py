from django.db import models

# Create your models here.

class Service(models.Model):
    SERVICE_CATEGORY= (
        ('Mechanical','Mechanical'),
        ('Electronics','Electronics'),
        ('Household','Household')
    )

    service_name = models.CharField(max_length=100, null=True)
    service_category = models.CharField(max_length=100, null=True, choices=SERVICE_CATEGORY)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.service_name

