from rest_framework import permissions
from posts.models import Follow

class IsFollowingPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method == 'POST' and Follow.following != request.user
