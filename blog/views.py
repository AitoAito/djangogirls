from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.utils import timezone

def get_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'index.html',{"posts": posts})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {})

def new_post(request):
    pass