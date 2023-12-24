# Generated by Django 3.2 on 2023-11-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='creado',
            field=models.DateTimeField(auto_now_add=True, default='2023-11-23', verbose_name='creado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='noticia',
            name='modificado',
            field=models.DateTimeField(auto_now=True, verbose_name='modificado'),
        ),
    ]
