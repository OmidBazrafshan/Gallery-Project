from django.shortcuts import render
from articles.models import Article
from .forms import ArticleForm ,CommentForm ,GalleryForm


def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ArticleForm()

    articles = Article.objects.filter(is_active = True)
    context ={
        'articles': articles, 
        'form': form
    }

    return render (request,'index.html', context)

def retrieve(request,id):
    article = Article.objects.get(id=id)
    gallery = GalleryForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        form2 = GalleryForm(request.POST)
        if form2.is_valid():
            form2.save()
    else:
        form = CommentForm()
        form2=GalleryForm()
        Comment_form = CommentForm()
        gallery = GalleryForm()
    context ={
        'article':article,
        'comment_form':Comment_form,
        'gallery':gallery
    }
    return render(request,'retrieve.html', context)