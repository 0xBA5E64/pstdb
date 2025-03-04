# Generated by Django 5.1.3 on 2024-11-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('realname', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('pub_date', models.DateTimeField()),
                ('youtube_id', models.CharField(max_length=11)),
                ('participants', models.ManyToManyField(to='podcast.participant')),
            ],
        ),
    ]
