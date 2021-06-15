from django.urls import path 
from .views import (NamePageListView)

urlpatterns=[
    path('' ,NamePageListView.as_view, name='name_page' )
]