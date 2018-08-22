# all_users/api views.py

from rest_framework import generics
from rest_framework import permissions

from django.contrib.auth import get_user_model
from .serializers import UserCreationSerializer
from .permissions import IsOwner

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):

	serializer_class = UserCreationSerializer
	permission_classes = [permissions.AllowAny,]


class UserDetailView(generics.RetrieveUpdateAPIView):

	serializer_class = UserCreationSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwner]

	def get_queryset(self, *args, **kwargs):
		return User.objects.all()



# detail view retrieve, update
# list view for admin
