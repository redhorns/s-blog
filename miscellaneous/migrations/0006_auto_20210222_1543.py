# Generated by Django 3.1 on 2021-02-22 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_auto_20210116_2216'),
        ('miscellaneous', '0005_boss_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Boss_Post',
            new_name='Home_Boss',
        ),
    ]