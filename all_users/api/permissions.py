from rest_framework import permissions

class IsCandidate(permissions.BasePermission):

	def has_permission(self, request, view):

		return request.user.is_candidate

class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.user.username == request.user.username

class IsOwner(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		return obj.username == request.user.username