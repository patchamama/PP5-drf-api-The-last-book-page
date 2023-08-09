# Generated by Django 3.2.20 on 2023-08-09 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='../default_profile_pi4td5.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='../No_image_available.svg_fqlc88.png', upload_to='images/'),
        ),
    ]