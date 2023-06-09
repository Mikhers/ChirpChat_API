# Generated by Django 4.2.1 on 2023-05-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="chat",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("user_name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("is_active", models.BooleanField(default=False, null=True)),
                (
                    "imagen",
                    models.ImageField(
                        blank=True, max_length=355, null=True, upload_to="media/"
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="solicitud",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                (
                    "my_self",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_solicitudes",
                        to="API_ChirpChat.usuario",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="solicitud_amistad",
                        to="API_ChirpChat.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="publicacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contenido", models.TextField()),
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="media/"),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                (
                    "my_self",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="API_ChirpChat.usuario",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="mensajes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("contenido", models.TextField()),
                ("leido", models.BooleanField(default=False)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                (
                    "id_chat",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="API_ChirpChat.chat",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="chat",
            name="user_id_1",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="my_self_chat",
                to="API_ChirpChat.usuario",
            ),
        ),
        migrations.AddField(
            model_name="chat",
            name="user_id_2",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="chat_amigo",
                to="API_ChirpChat.usuario",
            ),
        ),
        migrations.CreateModel(
            name="amigos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                (
                    "amigo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="amigo",
                        to="API_ChirpChat.usuario",
                    ),
                ),
                (
                    "my_self",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="my_self_amigos",
                        to="API_ChirpChat.usuario",
                    ),
                ),
            ],
        ),
    ]
