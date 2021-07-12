# Generated by Django 3.2.5 on 2021-07-11 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='E-mail')),
                ('comentario', models.TextField(max_length=255, verbose_name='Comentário')),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('publicacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]