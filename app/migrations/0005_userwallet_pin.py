# Generated by Django 4.2.8 on 2023-12-20 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwallet',
            name='pin',
            field=models.IntegerField(default=1111),
            preserve_default=False,
        ),
    ]
