from rest_framework import serializers

from .models import usuario, amigos, foto, solicitud, publicacion, mensajes, chat

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = "__all__"
        read_only_fields = ('created_at',)
class amigosSerializer(serializers.ModelSerializer):
    class Meta:
        model = amigos
        fields = "__all__"
        read_only_fields = ('created_at',)
class fotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = foto
        fields = "__all__"
        read_only_fields = ('created_at',)
class solicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = solicitud
        fields = "__all__"
        read_only_fields = ('created_at',)
class publicacionSerializer(serializers.ModelSerializer):
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