# Generated by Django 3.1 on 2021-02-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_author_author_sm'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
