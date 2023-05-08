from rest_framework import viewsets, permissions
from .models import usuario, amigos, solicitud, publicacion, mensajes, chat
from .serializers import usuarioSerializer, amigosSerializer, solicitudSerializer, publicacionSerializer, mensajesSerializer, chatSerializer
# Create your views here.


# class FotoViewSet(viewsets.ModelViewSet):
#     queryset = foto.objects.all()
#     permission_classes = [permissions.AllowAny]
#     serializer_class = fotoSerializer
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = usuarioSerializer
class AmigosViewSet(viewsets.ModelViewSet):
    queryset = amigos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = amigosSerializer
class solicitudViewSet(viewsets.ModelViewSet):
    queryset = solicitud.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = solicitudSerializer
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = publicacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = publicacionSerializer
class MensajesViewSet(viewsets.ModelViewSet):
    queryset = mensajes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = mensajesSerializer
class ChatViewSet(viewsets.ModelViewSet):
    queryset = chat.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = chatSerializer