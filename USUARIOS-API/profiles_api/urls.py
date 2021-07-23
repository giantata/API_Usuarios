from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('prueva-viewset', views.PruebaViewSet, basename='prueva-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)


urlpatterns = [
    path('prueba-view/', views.PruebaApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]