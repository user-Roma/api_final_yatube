from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """Gives permissions for safe methods for all."""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class AuthorOrIsAuthenticatedAndReadOnly(permissions.IsAuthenticated):
    """
    Gives permissions to use all methods for author
    and to use safe methods for authenticated.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
