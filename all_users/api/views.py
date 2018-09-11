# all_users/api views.py

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from .serializers import UserDisplaySerializer, UserCreationSerializer
from .permissions import IsOwner

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):

	serializer_class = UserCreationSerializer
	permission_classes = [permissions.AllowAny,]

	def post(self, request):

		serializer = UserCreationSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class UserDetailAPIView(generics.RetrieveUpdateAPIView):

	serializer_class = UserCreationSerializer
	permission_classes = [permissions.IsAuthenticated, IsOwner]

	def get_queryset(self, *args, **kwargs):
		return User.objects.all()

class UserListAdminAPIView(generics.ListAPIView):

	serializer_class = UserDisplaySerializer
	permission_classes = [permissions.IsAdminUser,]

	def get_queryset(self, *args, **kwargs):
		return User.objects.all()

class UserRetrieveAdminAPIView(generics.RetrieveAPIView):

	serializer_class = UserDisplaySerializer
	permission_classes = [permissions.IsAdminUser,]

	def get_queryset(self, *args, **kwargs):
		return User.objects.all()



# detail view retrieve, update
# list view for admin
