# Generated by Django 3.0.8 on 2020-08-04 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0011_auto_20200804_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ManyToManyField(to='photos.category'),
        ),
    ]
