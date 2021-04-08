from rest_framework.permissions import SAFE_METHODS, BasePermission


class PollPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        if request.method.upper() in SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class QuestionPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
