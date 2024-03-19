from rest_framework.serializers import ModelSerializer
from .models import Refuel

class RefuelSerializer(ModelSerializer):
    class Meta:
        model = Refuel
        fields = '__all__'
        depth = 1