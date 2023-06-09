from rest_framework import serializers
from .models import usuario, amigos, solicitud, publicacion, mensajes, chat
from drf_extra_fields.fields import Base64ImageField

class usuarioSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = usuario
        fields = "__all__"
        read_only_fields = ('created_at',)
class amigosSerializer(serializers.ModelSerializer):
    class Meta:
        model = amigos
        fields = "__all__"
        read_only_fields = ('created_at',)
class solicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = solicitud
        fields = "__all__"
        read_only_fields = ('created_at',)
class publicacionSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = publicacion
        fields = "__all__"
        read_only_fields = ('created_at',)
class mensajesSerializer(serializers.ModelSerializer):
    class Meta:
        model = mensajes
        fields = "__all__"
        read_only_fields = ('created_at',)
class chatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chat
        fields = "__all__"
        read_only_fields = ('created_at',)

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ["email", "password"]
