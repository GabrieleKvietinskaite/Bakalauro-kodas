# Generated by Django 3.1.2 on 2020-12-30 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20201230_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='competences',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
