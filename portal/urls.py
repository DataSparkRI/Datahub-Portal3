from django.urls import path, include
from portal import views

urlpatterns = [
        path('file_page/<path:slug>/', views.filepage, name='file_page'),
]
