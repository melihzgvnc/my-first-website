from django.urls import path
from .views import *

app_name = 'complaint'

urlpatterns = [
    path('index', complaint_index, name='index'),
    path('create', complaint_create, name='create'),

   
    #path('<slug:slug>/update', post_update, name='update'),
    path('<slug:slug>/delete', complaint_delete, name='delete'),
    path('<slug:slug>', complaint_detail, name='detail'),
]