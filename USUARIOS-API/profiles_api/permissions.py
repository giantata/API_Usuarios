from django.utils import tree
from rest_framework import permissions, request

class UpdateOwnProfile(permissions.BasePermission):
    """Permite a usuario editar su perfil"""

    def has_object_permission(self, request, view, obj):
        """Verfiica si usuario esta intentando editar su propio perfil"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Permite actualizar propio status Fedd"""

    def has_object_permission(self, request, view, obj):
        """Chequea su isuario esta intentando editar su propio Perfil"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile_id == request.user.id


