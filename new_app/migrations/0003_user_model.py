# Generated by Django 5.0.1 on 2024-02-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_alter_task_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('is_admin', models.BooleanField()),
            ],
        ),
    ]
