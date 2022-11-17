# Generated by Django 4.1 on 2022-09-01 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CALLES',
            fields=[
                ('calle', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Registros de calles')),
            ],
            options={
                'verbose_name': 'Calle registrada',
                'verbose_name_plural': 'Calles registradas',
                'ordering': ['calle'],
            },
        ),
        migrations.CreateModel(
            name='INFORMACION',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen del defecto')),
                ('callefinal', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.calles', verbose_name='Calles registradas')),
            ],
        ),
    ]
