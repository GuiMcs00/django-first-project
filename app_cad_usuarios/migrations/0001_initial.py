# Generated by Django 5.0.3 on 2024-03-05 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
