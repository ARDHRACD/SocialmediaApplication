# Generated by Django 4.1.4 on 2023-03-07 15:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mediaweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
