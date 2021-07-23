from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers, models, permissions

 
#(Definomos un APIView)

class PruebaApiView(APIView):
    """API View de prueba"""
    serializer_class = serializers.PruebaViewSerializer

    def get(self, request, format = None):
        """Retorna lista de carascteristicas del ApiView"""

        an_apiview = [
            'Usamos metodos HTTP con funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Django', 
            'Proporcina mayor control sobre la logica de la Aplicacion',
            'Está mapeado manualmente a los URLs'
        ]
        return Response({'message': "Prueba API's-VIEWs", 'an_apiview': an_apiview})
    
    def post(self, request):
        """Crea un mensaje con nuestro Nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'mesaage': message})

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk = None):
        """ACTUALIZA UN OBJETO"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk = None):
        """ACTUALIZACION PARCIAL DE UN OBJETO"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk = None):
        """BORRA UN OBJETO"""
        return Response({'method': 'DELETE'})

#(Definimos un ViewSet)

class PruebaViewSet(viewsets.ViewSet):
    """Testing API ViewSet"""
    serializer_class = serializers.PruebaViewSerializer

    def list(self, request):
        """Retorna mensaje Hola_ViewSet"""

        a_viewset = [
            'Usa acciones de ()list, create, retrieve, update, partial_update',
            'Automaticamente mapea a los URLs usando Routers',
            'Mas funcionalidad con menos codigo',
        ]
        return Response({'message': 'Prueba ViewSet', 'a_viewset': a_viewset})

    def create(self, request):
        """Creamos un nuevo mensaje de Hola_Prueba"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hola {name}"
            return Response({'message': message})
        
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk=None):
        """Obtiene un Objeto y su ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Actualiza un Objeto"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Actualiza parcialmete un Objeto"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Elimina un Objeto"""
        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Crea y Actualiza Perfiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """Crea Token de autenticación de Usuario"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Maneja el Crear, Leer, Actualizar el Profile FEED """

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permissions_class = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Setea el perfil de uauario, para el ususario q esta logueado"""
        serializer.save(user_profile = self.request.user)



