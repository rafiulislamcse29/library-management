# Generated by Django 4.2.13 on 2024-06-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='media/book/images/default.png', upload_to='media/book/images'),
        ),
    ]