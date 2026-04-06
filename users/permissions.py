from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsAnalyst(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'analyst']


class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['admin', 'analyst', 'viewer']


class RecordPermission(BasePermission):
    """
    Global permission for records
    """

    def has_permission(self, request, view):

        # Read-only methods (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return request.user.role in ['admin', 'analyst', 'viewer']

        # Write operations
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return request.user.role == 'admin'

        return False