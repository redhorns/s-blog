# Generated by Django 3.1 on 2021-02-22 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miscellaneous', '0002_home_most_popular'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_most_popular',
            name='index',
        ),
    ]