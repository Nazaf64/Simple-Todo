from django.db import models
from datetime import datetime
import uuid

# Create your models here.
class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task = models.CharField(max_length=200)
    created_instance = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.task
