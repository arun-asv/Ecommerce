# Generated by Django 3.2 on 2021-06-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210609_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='num',
            field=models.IntegerField(),
        ),
    ]
