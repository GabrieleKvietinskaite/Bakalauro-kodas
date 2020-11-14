# Generated by Django 3.1.2 on 2020-11-14 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_scenario_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='level',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='app.role_level'),
            preserve_default=False,
        ),
    ]
