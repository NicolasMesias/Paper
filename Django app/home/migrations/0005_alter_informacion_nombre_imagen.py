# Generated by Django 4.1 on 2022-09-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_informacion_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='nombre_imagen',
            field=models.CharField(max_length=100, null=True, verbose_name='Nombre de la imagen'),
        ),
    ]
