from django.db import models
from django.contrib.auth.models import User
from course.models import Course

class Article(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()
    img = models.ImageField(upload_to='articles')
    excerpt = models.CharField(max_length=500)


    def __str__(self) -> str:
        return self.title