# Generated by Django 3.2 on 2021-06-09 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20210608_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mobile',
            new_name='number',
        ),
        migrations.RemoveField(
            model_name='otp',
            name='number',
        ),
        migrations.AddField(
            model_name='otp',
            name='num',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
