# Generated by Django 4.1 on 2022-10-05 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_informacion_upload_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacion',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen del defecto'),
        ),
    ]
