# Generated by Django 4.1.2 on 2022-10-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='welcome to my homepage!', max_length=100),
        ),
    ]
