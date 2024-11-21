# Generated by Django 5.1.3 on 2024-11-21 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='description',
            field=models.CharField(default='', max_length=240),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episode',
            name='pub_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='participant',
            name='description',
            field=models.CharField(blank=True, max_length=240),
        ),
        migrations.AlterField(
            model_name='participant',
            name='realname',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]