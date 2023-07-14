from django.shortcuts import render
from blogs.models import Post

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}     #can use allPosts as variable
    return render(request,'blog/blogHome.html',context)