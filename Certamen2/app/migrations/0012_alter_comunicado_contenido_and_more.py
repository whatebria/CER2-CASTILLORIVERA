# Generated by Django 4.2.6 on 2023-10-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_comunicado_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='contenido',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(upload_to='images/%Y/%m', verbose_name='Imagen'),
        ),
    ]
