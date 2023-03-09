
from django.urls import path
from .views import *
urlpatterns = [
    path('', Createaccount.as_view(), name="createuser")
]
