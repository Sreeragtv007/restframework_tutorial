from .models import *
from rest_framework.serializers import ModelSerializer


class Studentserializer(ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'