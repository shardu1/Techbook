from django.shortcuts import render

# Create your views here.
def blogs_index(request):
    return render(request,'index.html')