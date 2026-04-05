from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminAnalystOrOwner(BasePermission):

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False    # check if user if logged in

        if request.user.role == 'admin':
            return True     # if role is admin it gives full access

        if request.user.role == 'analyst':
            return request.method in SAFE_METHODS       # if role is admin it gives read only access

        if request.user.role == 'user':
            return True     # if role is user it allows full access

        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True

        if request.user.role == 'analyst':
            return request.method in SAFE_METHODS

        if request.user.role == 'user':
            return obj.created_by == request.user       # give access to only user's own data

        return False