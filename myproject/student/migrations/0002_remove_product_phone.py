# Generated by Django 4.1 on 2023-06-19 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='phone',
        ),
    ]
