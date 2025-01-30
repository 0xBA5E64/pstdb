# Generated by Django 5.1.3 on 2025-01-30 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0003_alter_episode_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EpisodeSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('time_start', models.IntegerField()),
                ('time_end', models.IntegerField()),
                ('episode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='podcast.episode')),
            ],
        ),
    ]
