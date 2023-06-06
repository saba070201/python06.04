from django.shortcuts import render,get_object_or_404,redirect
from articleapp.models import *
from django.contrib.auth.decorators import login_required
from articleapp.forms import * 
def home(request):
    data=Article.objects.filter(published=True)
    return render(request,'articleapp/home.html',{'articles':data})


def view_art(request,art_id):
    data=get_object_or_404(Article,pk=art_id,published=True)
    return render(request,'articleapp/view_art.html',{'article':data})


@login_required
def create_article(request):
    if request.method=='GET':
        return render(request,'articleapp/create_article.html',{'form':CreateArticleForm()})
    else: 
        try:
            form=CreateArticleForm(request.POST,request.FILES)
            newart=form.save(commit=False)
            newart.author=request.user
            form.save()
            return redirect('articleapp:home')
        except ValueError:
            return render(request,'articleapp/create_article.html',{'form':CreateArticleForm(),'error':'неккоректные значения'})

@login_required
def change_article(request,art_id):
    article=get_object_or_404(Article,pk=art_id,author=request.user)
    if request.method=='GET':
          return render(request,'articleapp/change_article.html',{'article':article})
    else: 
        try:
            form=CreateArticleForm(request.POST,request.FILES,instance=article)
            form.save()
            return redirect('articleapp:home')
        except ValueError:
            return render(request,'articleapp/change_article.html',{'error':'неккоректные значения','article':article})


@login_required
def view_article(request,art_id): # переименовать view_art
    article_=get_object_or_404(Article,pk=art_id,author=request.user)
    articleblocks=ArticlesBlock.objects.filter(article=art_id)
    return render(request,'articleapp/view_article.html',{'article':article_,'articleblocks':articleblocks}) 

@login_required
def delete_article(request,art_id):
    article=get_object_or_404(Article,pk=art_id,author=request.user)
    if request.method=='POST':
        article.published=False
        article.save()
        return redirect('articleapp:home')
