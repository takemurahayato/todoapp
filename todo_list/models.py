from django.db import models


PRIORITY_CHOICES = (
    ('1', '高'),
    ('2', '中'),
    ('3', '低')
)
# Create your models here.

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + ' | ' + str(self.completed)

class Priority(models.Model):
    priority = models.CharField(max_length=30, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.priority