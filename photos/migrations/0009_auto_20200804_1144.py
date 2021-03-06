# Generated by Django 3.0.8 on 2020-08-04 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0008_remove_image_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='category',
            new_name='image_category',
        ),
        migrations.AddField(
            model_name='image',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
