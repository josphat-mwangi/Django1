# Generated by Django 3.0.8 on 2020-08-03 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='categoryname',
            new_name='name',
        ),
    ]
