# Generated by Django 3.0.2 on 2020-01-09 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200109_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='user_1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tea',
            name='user_2',
            field=models.CharField(max_length=50),
        ),
    ]
