# Generated by Django 3.1 on 2021-02-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0009_newsletter_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram_Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='instagram')),
            ],
        ),
    ]
