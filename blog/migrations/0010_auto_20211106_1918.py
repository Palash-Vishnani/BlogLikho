# Generated by Django 3.2.5 on 2021-11-06 13:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20211106_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content1',
            field=models.TextField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='heading1',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
