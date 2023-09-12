from django.shortcuts import render
from userauth.models import Batch, UserDetail
from routine.models import Routine

def routine_view(request):
    user =request.user
    auser = UserDetail.objects.get(user=user)
    routine = Routine.objects.filter(batch =auser.batch)
    if routine.first():
        routine = Routine.objects.get(batch =auser.batch)
    
    return render(request,'routine/routine.html',{'routine':routine})
