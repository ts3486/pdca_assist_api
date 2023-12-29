from rest_framework import serializers
from .models import Cycle
class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ["name", "status", "category", "problem", "do", "action", "check", "created_at", "updated_at"]