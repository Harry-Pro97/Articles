from django.urls import path
from . import views
urlpatterns=[
    path('',views.index),
    path('one/<int:Hari>',views.result,name='Description')
]