from django.urls import path
from . import views 

urlpatterns=[
    path("",views.newsHome,name='newsHome'),
    # path("get/<str:sluge>",views.getNews,name='getNews'),
    path('<str:slug>', views.newsPost ,name="newsPost"),
    path("s/search", views.search ,name="search"),
]