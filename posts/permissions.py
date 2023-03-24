from rest_framework import permissions


# Overriding BasePermission For Our Custom Permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    # Has Permission works only on list views
    def has_permission(self, request, view):
        # Authenticated users only can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_psermission(self, request, view, obj):
        # Has Permission works on list views & Detail View
        # Read permissions are allowed to any request so we'll always
        # allow GET, HEAD, or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to the author of a post
        return obj.author == request.user
