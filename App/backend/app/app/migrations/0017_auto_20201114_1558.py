# Generated by Django 3.1.2 on 2020-11-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_player_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='results',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]