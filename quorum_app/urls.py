# urls.py

from django.urls import path
from .views import legislator_vote_stats, bill_vote_stats, all_stats


urlpatterns = [
    path('legislator_vote_stats/', legislator_vote_stats, name='legislator_vote_stats'),
    path('bill_vote_stats/', bill_vote_stats, name='bill_vote_stats'),
    path('all_stats/', all_stats, name='all_stats'),
  
]
