# Generated by Django 4.2.6 on 2023-10-22 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_entidad_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entidad',
            name='logo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
