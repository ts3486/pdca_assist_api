from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone

class Cycle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 180, default="Tao")
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length = 180, default="NEW")
    updated_at = models.DateTimeField(default=timezone.now)
    # user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.name