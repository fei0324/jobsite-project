# candidates/api views.py

from rest_framework import generics
from rest_framework import permissions

from candidates.models import CandidateProfile
from .serializers import CandidateProfileSerializer

class CandidateListAPIView(generics.ListAPIView):

	serializer_class = CandidateProfileSerializer

	def get_queryset(self, *args, **kwargs):
		return CandidateProfile.objects.all()

class CandidateCreateAPIView(generics.CreateAPIView):

	serializer_class = CandidateProfileSerializer
	permission_classes = [permissions.IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class CandidateRetrieveAPIView(generics.RetrieveAPIView):

	serializer_class = CandidateProfileSerializer

	def get_queryset(self, *args, **kwargs):
		return CandidateProfile.objects.all()