# Generated by Django 4.2.3 on 2023-09-29 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppComunidad', '0002_comunidad_precio_preguntascom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunidad',
            name='precio',
            field=models.CharField(max_length=10),
        ),
    ]
