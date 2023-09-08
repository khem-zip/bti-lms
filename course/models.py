from django.db import models
from userauth.models import Batch
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=200)
    batch = models.ManyToManyField(Batch)
    teacher = models.ManyToManyField(User)
    pic = models.ImageField(null=False, upload_to='coursepics')
    cr_hours = models.IntegerField(default=0)
    desc = models.TextField(null=True)

    def __str__(self):
        return self.name
