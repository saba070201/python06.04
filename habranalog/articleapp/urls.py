from django.urls import path
from articleapp.views import *
app_name='articleapp'
urlpatterns=[
    path('',home,name='home'),
    path('view-article-<int:art_id>',view_art,name='view_art')
]