# In your traveljournal/urls.py or journalapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('journals/<int:journal_id>/', views.journal_detail, name='journal_detail'),
    path('create_journal/', views.create_journal, name='create_journal'),
    # Add more URL patterns for other views as needed
]
