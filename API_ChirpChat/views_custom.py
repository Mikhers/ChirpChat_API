from .serializers import AuthSerializer,amigosSerializer, solicitudSerializer, chatSerializer
from .models import usuario, amigos,solicitud, chat
from django.contrib.auth.hashers import check_password
from rest_framework import status
from rest_framework import generics
from django.db.models import Q
from rest_framework.views import APIView 
from rest_framework.response import Response


class ListaAmigosViewSet(generics.ListAPIView):
    serializer_class = amigosSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = amigos.objects.filter(Q(my_self=id) | Q(amigo=id))
        return queryset
    
class ListasolicitudViewSet(generics.ListAPIView):
    serializer_class = solicitudSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = solicitud.objects.filter(Q(my_self=id) | Q(user=id))
        return queryset

class ListaChatViewSet(generics.ListAPIView):
    serializer_class = chatSerializer
    def get_queryset(self):
        id = self.kwargs['id']
        queryset = chat.objects.filter(Q(user_id_1=id) | Q(user_id_2=id))
        return queryset


class AuthViewSet(APIView):
    serializer_class = AuthSerializer

    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = list(usuario.objects.filter(email=email).values())[0]
            if user is not None:
                es_correcto = check_password(password, user['password'])
                if es_correcto:
                    return Response(user, status=status.HTTP_202_ACCEPTED)
                return Response({'message': 'Credenciales invalidas'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response({'message': 'El usuario no se encuentra registrado'}, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response({'message': 'El usuario no se encuentra registrado'}, status=status.HTTP_401_UNAUTHORIZED)

