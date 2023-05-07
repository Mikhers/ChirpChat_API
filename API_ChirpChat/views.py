from rest_framework import viewsets, permissions
from .models import usuario, amigos, foto, solicitud, publicacion, mensajes, chat
from .serializers import usuarioSerializer, amigosSerializer, fotoSerializer, solicitudSerializer, publicacionSerializer, mensajesSerializer, chatSerializer
# Create your views here.


class FotoViewSet(viewsets.ModelViewSet):
    queryset = foto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = fotoSerializer


# from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response

# class FotoUploadView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
    
#     def post(self, request, *args, **kwargs):
#         serializer = fotoSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)

# class FotoDetailView(APIView):
    
#     def get(self, request, id, format=None):
#         f = foto.objects.get(id=id)
#         imagen_url = f.imagen.url
#         return Response({'imagen_url': imagen_url})

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