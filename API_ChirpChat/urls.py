from rest_framework import routers
from .views import UsuarioViewSet, AmigosViewSet, FotoViewSet, solicitudViewSet, PublicacionViewSet, MensajesViewSet, ChatViewSet
router = routers.DefaultRouter()

router.register('usuario', UsuarioViewSet, 'usuario')
router.register('amigo', AmigosViewSet, 'amigo')
router.register('foto', FotoViewSet, 'foto')
router.register('solicitudes', solicitudViewSet, 'solicitudes')
router.register('publicacion', PublicacionViewSet, 'publicacion')
router.register('mensaje', MensajesViewSet, 'mensaje')
router.register('chat', ChatViewSet, 'chat')

urlpatterns = router.urls