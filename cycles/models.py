from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

class Cycle(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 180, default="title")
    status = models.CharField(max_length = 180, default="NEW")
    category = models.PositiveIntegerField(default=0)
    problem_description = models.CharField(max_length = 500, default="")
    plan_description = models.CharField(max_length = 500, default="")
    do_description = models.CharField(max_length = 500, default="")
    check_description = models.CharField(max_length = 500, default="")
    action_description = models.CharField(max_length = 500, default="")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.title