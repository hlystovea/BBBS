from rest_framework.permissions import BasePermission


class IsUsersCity(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.has_perm('api.view_in_all_cities'):
            return obj.city == request.user.city
        return True
