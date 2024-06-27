# Generated by Django 5.0.6 on 2024-06-22 05:57

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='name')),
                ('body', models.CharField(db_index=True, max_length=500, verbose_name='body')),
                ('image', cloudinary.models.CloudinaryField(blank=True, db_index=True, max_length=255, null=True, verbose_name='image')),
                ('count', models.IntegerField(blank=True, default=0, verbose_name='count')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated datetime')),
            ],
        ),
    ]
