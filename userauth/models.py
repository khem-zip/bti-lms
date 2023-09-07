from django.db import models
from django.contrib.auth.models import User



class Batch(models.Model):
    class Meta:
        verbose_name_plural = "Batches"

    name = models.CharField(max_length=40)
    year = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    



# userdetail
class UserDetail(models.Model):
    user = models.OneToOneField(User, related_name='userdetail' , on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(null=True)
    contact = models.CharField(max_length=10)
    pp = models.ImageField(null=True, upload_to='pp', blank=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' '  + self.last_name
    