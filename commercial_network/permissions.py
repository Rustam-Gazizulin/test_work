from rest_framework.permissions import BasePermission


class ProviderPermission(BasePermission):
    message = "Только штатные сотрудники (статус is_staff) имеют доступ!!!"

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False
