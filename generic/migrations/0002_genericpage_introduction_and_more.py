# Generated by Django 4.1.2 on 2022-10-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='introduction',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='genericpage',
            name='banner_title',
            field=models.CharField(default='welcome to my generic page!', max_length=100),
        ),
    ]
