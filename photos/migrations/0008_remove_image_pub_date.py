# Generated by Django 3.0.8 on 2020-08-04 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_auto_20200804_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pub_date',
        ),
    ]
