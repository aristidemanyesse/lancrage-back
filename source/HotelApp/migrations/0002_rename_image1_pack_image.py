# Generated by Django 4.2.8 on 2023-12-27 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='image1',
            new_name='image',
        ),
    ]