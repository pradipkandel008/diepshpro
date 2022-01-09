from django.core.exceptions import RequestAborted
from django.forms import ModelForm, fields
from professionals.models import Servc

class ServiceForm(ModelForm):
    class Meta:
        model = Servc
        fields = '__all__'
        exclude = ['service_user']