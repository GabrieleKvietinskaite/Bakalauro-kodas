# Generated by Django 3.1.2 on 2020-11-14 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20201114_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='dd',
        ),
    ]
