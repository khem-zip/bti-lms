from django.shortcuts import render, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

def article_detail_view(request,id):
    article = get_object_or_404(Article,id=id)
    return  render(request, 'article/detail.html',{'article':article})

def add_article_view(request):
    form = ArticleForm(user=request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, user=request.user )
        if form.is_valid():
            fm = form.save(commit=False)
            fm.author = request.user
            form.save()
            messages.success(request, 'Article successfully published.')
        else:
            messages.error(request, 'Something went wrong.')


    context = {
        'form':form
    }
    return render(request, 'article/add_article.html', context)