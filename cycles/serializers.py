from rest_framework import serializers
from .models import Cycle
class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ["id", "title", "status", "category", "problem_description", "plan_description", "do_description", "action_description", "check_description", "created_at", "updated_at"]