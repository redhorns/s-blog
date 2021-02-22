# Generated by Django 3.1 on 2020-12-30 20:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(blank=True, max_length=10, null=True)),
                ('section_name', models.CharField(blank=True, max_length=100, null=True)),
                ('section_identifier', models.CharField(blank=True, max_length=100, null=True)),
                ('section_info', models.TextField(blank=True, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=250, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(blank=True, max_length=10, null=True)),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('intro', models.TextField(blank=True, null=True)),
                ('detail', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('special_blog', models.CharField(blank=True, max_length=25, null=True)),
                ('special_image', models.ImageField(blank=True, null=True, upload_to='blog_images')),
                ('date', models.CharField(blank=True, max_length=100, null=True)),
                ('comment_count', models.CharField(blank=True, max_length=100, null=True)),
                ('read_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=300, null=True)),
                ('meta_description', models.TextField(blank=True, null=True)),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel.blog_section')),
            ],
        ),
    ]
