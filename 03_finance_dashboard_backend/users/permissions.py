from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrAnalyst(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.role == 'admin':
            return True

        if request.user.role == 'analyst' and request.method in SAFE_METHODS:
            return True

        return False