# Generated by Django 4.2.8 on 2023-12-20 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_transaction_credit_transaction_debit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='credit',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='debit',
        ),
    ]
