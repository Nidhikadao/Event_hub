from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    
    path('postComment',views.postComment,name='postComment'),
    path('', views.orghome,name='orghome'),
    path('<str:slug>', views.orgpost,name='orgpost'),
    #path('search/<str:slug>', views.search,name='search'),
    #path("upload/", custom_upload_Post, name="custom_upload_file"),
    
    
    
]
