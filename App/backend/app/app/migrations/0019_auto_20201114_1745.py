# Generated by Django 3.1.2 on 2020-11-14 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20201114_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='hypothesis',
            new_name='received_points',
        ),
    ]
