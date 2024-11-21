# biblioteca/permissions.py
from rest_framework.permissions import BasePermission

class IsColecionador(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Verifica se o usuário autenticado é o colecionador da coleção
        return obj.colecionador == request.user