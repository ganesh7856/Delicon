# Generated by Django 3.0.8 on 2020-07-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='journeyfrom',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='registeruser',
            name='journeyto',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AddField(
            model_name='registeruser',
            name='train_name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
