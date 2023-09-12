from django.db import models
from userauth.models import Batch
from django.contrib.auth.models import User
from course.models import Course

class Routine(models.Model):
    batch = models.ForeignKey(Batch,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.batch.name
    
    # for using in template
    @property
    def routinedetails(self):
        return RoutineDetail.objects.filter(routine=self.id)
    
    @property
    def routinedays(self):
        return RoutineDetail.objects.filter(routine=self.id).values('day').distinct()


class RoutineDetail(models.Model):
    DAYS_OF_WEEK_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
        ]
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    time = models.CharField(max_length=11)
    day = models.CharField(
        max_length=9,
        choices=DAYS_OF_WEEK_CHOICES,
        default='Monday',  
    )
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.day

