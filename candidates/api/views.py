# candidates/api views.py
from rest_framework import generics

from candidates.models import CandidateProfile
from .serializers import CandidateProfileSerializer

class CandidateListAPIView(generics.ListAPIView):

	serializer_class = CandidateProfileSerializer

	def get_queryset(self, *args, **kwargs):
		return CandidateProfile.objects.all()

class CandidateCreateAPIView(generics.CreateAPIView):

	serializer_class = CandidateProfileSerializer