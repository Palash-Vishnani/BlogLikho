# Generated by Django 3.2.7 on 2021-10-09 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='Promotional Blogs', max_length=200),
        ),
    ]
