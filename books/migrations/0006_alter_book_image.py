# Generated by Django 4.2.13 on 2024-06-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(default='book/images/default.png', upload_to='book/images'),
        ),
    ]