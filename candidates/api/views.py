# candidates/api views.py

from rest_framework import generics
from rest_framework import permissions

from candidates.models import CandidateProfile
from .serializers import CandidateProfileSerializer
from all_users.api.permissions import IsCandidate, IsOwnerOrReadOnly

class CandidateListAPIView(generics.ListAPIView):

	serializer_class = CandidateProfileSerializer

	def get_queryset(self, *args, **kwargs):
		return CandidateProfile.objects.all()

class CandidateCreateAPIView(generics.CreateAPIView):

	serializer_class = CandidateProfileSerializer
	permission_classes = [permissions.IsAuthenticated, IsCandidate,]

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class CandidateDetailView(generics.RetrieveUpdateAPIView):

	serializer_class = CandidateProfileSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

	def get_queryset(self, *args, **kwargs):
		return CandidateProfile.objects.all()

# class CandidateUpdateAPIView(generics.UpdateAPIView):

# 	serializer_class = CandidateProfileSerializer
# 	permissions_classes = [permissions.IsAuthenticated, IsOwner,]

# 	def get_queryset(self, *args, **kwargs):
# 		return CandidateProfile.objects.all()