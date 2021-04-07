from django.db import models
from uuid import uuid4


# Create your models here.
class Poll(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=1024)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    description = models.TextField(max_length=4096)

    def __str__(self):
        return self.name


class Question(models.Model):
    # type choices
    TYPE_CHOICES = (
        ('TEXT', 'Text'),
        ('ONE', 'Choice of one option'),
        ('SEVERAL', 'Choice of several options'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField(max_length=4096)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, blank=True, null=True)
