# Generated by Django 3.0.8 on 2020-08-13 20:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paperTrade', '0005_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='user',
        ),
        migrations.AddField(
            model_name='stock',
            name='user',
            field=models.ManyToManyField(related_name='stocks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ManyToManyField(related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
    ]
