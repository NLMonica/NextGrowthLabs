# Generated by Django 5.0.1 on 2024-02-03 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
