# Generated by Django 5.0 on 2024-03-04 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactenquiry',
            old_name='Name',
            new_name='name',
        ),
    ]
