# Generated by Django 5.0.1 on 2024-01-31 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SafariLinkApp', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
