# Generated by Django 2.2 on 2019-04-28 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedPill', '0006_location_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='has_been_seen',
            field=models.BooleanField(default=False),
        ),
    ]
