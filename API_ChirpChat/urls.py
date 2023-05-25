from rest_framework import routers
from django.urls import path
from .views_custom import AuthViewSet, ListaAmigosViewSet, ListaChatViewSet, ListasolicitudViewSet
from .views import UsuarioViewSet, AmigosViewSet, solicitudViewSet, PublicacionViewSet, MensajesViewSet, ChatViewSet
router = routers.DefaultRouter()

router.register('usuario', UsuarioViewSet, 'usuario')
router.register('amigo', AmigosViewSet, 'amigo')
router.register('solicitudes', solicitudViewSet, 'solicitudes')
router.register('publicacion', PublicacionViewSet, 'publicacion')
router.register('mensaje', MensajesViewSet, 'mensaje')
router.register('chat', ChatViewSet, 'chat')

urlpatterns = router.urls

urlpatterns += [
    path('login/', AuthViewSet.as_view(), name='login'),
    path('lista-amigos/<str:id>/', ListaAmigosViewSet.as_view(), name='lista-de-amigos'),
    path('lista-publicaciones/<str:id>/', ListaAmigosViewSet.as_view(), name='lista-de-publicaciones'),
    path('lista-solicitudes/<str:id>/', ListasolicitudViewSet.as_view(), name='lista-de-solicitudes'),
    path('lista-chats/<str:id>/', ListaChatViewSet.as_view(), name='lista-de-chats'),
]