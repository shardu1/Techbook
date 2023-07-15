from django.shortcuts import render , HttpResponse
from blogs.models import Post

# Create your views here.

def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts':allPosts}     #can use allPosts as variable in blogHOme.html
    return render(request,'blog/blogHome.html',context)

def testing(request):
    return HttpResponse("testing")