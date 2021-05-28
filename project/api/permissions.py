<<<<<<< HEAD
from rest_framework import permissions


class IsUsersCity(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.city == request.user.profile.city
=======
from rest_framework.permissions import BasePermission


class IsUsersCity(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('api.view_in_all_cities'):
            return obj.city == request.user.profile.city
        return True
>>>>>>> main
