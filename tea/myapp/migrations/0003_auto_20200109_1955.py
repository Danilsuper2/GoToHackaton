# Generated by Django 3.0.2 on 2020-01-09 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200109_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='user_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='myapp.User'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='user_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='myapp.User'),
        ),
    ]