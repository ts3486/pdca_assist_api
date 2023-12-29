from rest_framework import serializers
from .models import Cycle
class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ["name", "status", "user", "created_at", "updated_at"]