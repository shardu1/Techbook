from django.urls import path
from . import views 

urlpatterns=[
    path("",views.blogs_index,name='blogs_index')
]