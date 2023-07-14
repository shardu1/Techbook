from django.urls import path
from . import views 

urlpatterns=[
    path("",views.newsHome,name='newsHome'),
    path("technology",views.technology,name='technology'),
    path('<str:slug>', views.newsPost ,name="newsPost")
]