from django.core.exceptions import RequestAborted
from django.forms import ModelForm, fields
from admins.models import Service

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'