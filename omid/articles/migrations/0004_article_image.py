# Generated by Django 4.0.2 on 2022-06-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_tedad'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='article-images'),
            preserve_default=False,
        ),
    ]
