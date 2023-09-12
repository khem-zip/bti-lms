from django.shortcuts import render
from .models import NoticeBoard
from datetime import date



def allnotice_view(request):
    notices = NoticeBoard.objects.all().order_by('-id')
    today = date.today()
    return render(request,'notice/notice.html',{'notices':notices, 'today':today})