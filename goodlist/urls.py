from django.urls import path
from .views import *
urlpatterns = [

    path('deleteList',deleteList),
    path('getdetail', getdetail),
    path('addList',addList),
    path('getList', getList),


]