# Generated by Django 3.1 on 2021-01-31 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_userprofile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
