# Generated by Django 3.0.5 on 2020-04-21 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_musician_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]