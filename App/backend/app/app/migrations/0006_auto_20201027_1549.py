# Generated by Django 3.1.2 on 2020-10-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='started_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
