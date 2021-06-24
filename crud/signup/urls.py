from django.contrib import admin
from django.urls import path
from . import views
from signup.views import *

urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('detail/<int:id>', detail, name="detail"),
    path('edit/<int:id>', edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]