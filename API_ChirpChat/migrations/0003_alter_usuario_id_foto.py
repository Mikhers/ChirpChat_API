# Generated by Django 4.2.1 on 2023-05-07 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("API_ChirpChat", "0002_rename_mensages_mensajes_remove_foto_user_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="id_foto",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="API_ChirpChat.foto",
            ),
        ),
    ]