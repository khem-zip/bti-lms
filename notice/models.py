from django.db import models
from django.contrib.auth.models import User

class NoticeBoard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    subject =models.CharField(max_length=300)
    content = models.TextField()
    file = models.FileField(upload_to='notices', null=True, blank=True)

    def __str__(self) -> str:
        return self.subject