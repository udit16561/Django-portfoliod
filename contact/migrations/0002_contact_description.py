# Generated by Django 5.0 on 2024-02-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Description',
            field=models.TextField(default='none'),
        ),
    ]