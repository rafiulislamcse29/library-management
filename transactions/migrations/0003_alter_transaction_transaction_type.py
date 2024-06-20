# Generated by Django 4.2.13 on 2024-06-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_remove_transaction_loan_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Add Balance'), (2, 'Booked'), (3, 'Return')], null=True),
        ),
    ]
