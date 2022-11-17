# Generated by Django 4.1 on 2022-09-26 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_informacion_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacion',
            name='nombre_imagen',
            field=models.CharField(max_length=100, null=True, verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='informacion',
            name='resultado',
            field=models.CharField(max_length=20, null=True, verbose_name='Resultado del analis'),
        ),
        migrations.AddField(
            model_name='informacion',
            name='upload_to',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='calles',
            name='calle',
            field=models.CharField(max_length=70, primary_key=True, serialize=False, verbose_name='Registros de calles'),
        ),
    ]
