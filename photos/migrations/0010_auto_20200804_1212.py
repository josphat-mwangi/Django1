# Generated by Django 3.0.8 on 2020-08-04 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0009_auto_20200804_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image_category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_location',
            new_name='location',
        ),
    ]
