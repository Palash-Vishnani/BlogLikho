# Generated by Django 3.2.7 on 2021-10-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
