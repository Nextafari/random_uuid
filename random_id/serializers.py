from rest_framework import serializers
from .models import RandomId

class RandomIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RandomId
        fields = "__all__"