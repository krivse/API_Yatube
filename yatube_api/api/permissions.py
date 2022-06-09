from rest_framework import permissions


class IsFollowingPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if serializer.instance.following != self.request.user:
            return True