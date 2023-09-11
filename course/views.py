from django.shortcuts import render, get_object_or_404
from .models import Course
from userauth.models import UserDetail, Batch
from note.models import Note
from article.models import Article

def course_view(request):
    user = request.user
    acuser = UserDetail.objects.get(user=user)
    courses = Course.objects.filter(batch=acuser.batch)
    print(courses)
    return render(request,'course/course.html',{'courses':courses})

def course_detail_view(request,id):
    course = get_object_or_404(Course,id=id)
    notes = Note.objects.filter(course=course)
    articles = Article.objects.filter(course=course).order_by('-id')


    context={
        'course':course,
        'notes':notes,
        'articles':articles
    }
    return render(request, 'course/detail.html', context)
