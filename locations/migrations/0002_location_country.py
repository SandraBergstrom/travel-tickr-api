# Generated by Django 3.2.19 on 2023-07-01 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.CharField(default='Unknown', max_length=150),
        ),
    ]