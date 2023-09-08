from django.db import models
from course.models import Course
from django.contrib.auth.models import User

class Note(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='notefiles')
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

