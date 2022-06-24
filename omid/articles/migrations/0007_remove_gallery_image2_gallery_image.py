# Generated by Django 4.0.2 on 2022-06-18 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='image2',
        ),
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default=1, upload_to='article-images'),
            preserve_default=False,
        ),
    ]
