# Generated by Django 3.1.2 on 2020-10-27 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to=settings.AUTH_USER_MODEL)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='app.scenario')),
                ('questions', models.CharField(max_length=100)),
                ('received_points', models.CharField(max_length=100)),
                ('maximum_points', models.CharField(max_length=100)),
                ('hypothesis', models.CharField(max_length=100)),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
        ),
    ]
