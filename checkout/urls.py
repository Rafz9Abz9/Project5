from django.urls import path
from . import views

#url patterns here
urlpatterns = [
    path('', views.checkout, name='checkout'),
]