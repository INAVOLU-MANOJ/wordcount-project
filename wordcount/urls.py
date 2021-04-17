from django.urls import path
from . import look
urlpatterns = [
    path('',look.homepage,name='home'),
    path('counts/',look.count,name='count'),
    path('about/',look.about,name='about')
]
