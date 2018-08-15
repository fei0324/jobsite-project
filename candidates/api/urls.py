# candidate/api urls.py

from django.urls import path

from .views import (
	CandidateListAPIView,
	CandidateCreateAPIView,
	)


app_name = 'candidate-api'

urlpatterns = [
	path('', CandidateListAPIView.as_view(), name='list'),
	path('create/', CandidateCreateAPIView.as_view(), name='create'),
]