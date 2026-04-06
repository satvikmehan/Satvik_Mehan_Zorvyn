from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'analyst']


class IsViewer(BasePermission):
    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        if not request.user.is_active:
            return False

        return request.user.role in ['viewer', 'analyst', 'admin']


class RecordPermission(BasePermission):
    """
    Global permission for records
    """

    def has_permission(self, request, view):
        user = request.user

        # Not logged in
        if not user or not user.is_authenticated:
            return False
        
        #Inactive user
        if not user.is_active:
            return False

        # Read-only methods (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return user.role in ['admin', 'analyst', 'viewer']

        # Write operations
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return user.role == 'admin'

        return False