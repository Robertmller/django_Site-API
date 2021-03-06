# Generated by Django 3.2.5 on 2021-07-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=15, unique=True, verbose_name='Nome Completo')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('tel', models.IntegerField(unique=True, verbose_name='Celular')),
            ],
        ),
    ]
