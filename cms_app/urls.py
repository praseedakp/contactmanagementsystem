from django.urls import path
from .views import *

urlpatterns=[
    path('new/',newpage),
    path('regfunction/',regfunction),
    path('disp/',display),
    path('delete/<int:id>',delete),
    path('edit/<int:id>',edit)


]