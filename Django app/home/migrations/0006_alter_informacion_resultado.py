# Generated by Django 4.1 on 2022-09-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_informacion_nombre_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='resultado',
            field=models.CharField(max_length=50, null=True, verbose_name='Resultado del analis'),
        ),
    ]
