from django.shortcuts import render

# Create your views here.
def news_index(request):
    return render(request,'news/n-index.html')

def post_page(request):
    return render(request,'news/post-page.html')