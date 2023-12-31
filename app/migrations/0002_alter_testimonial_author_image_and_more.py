# Generated by Django 4.2.1 on 2023-06-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='author_image',
            field=models.ImageField(upload_to='testimonial_images'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
