# Generated by Django 4.1.2 on 2022-10-22 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0004_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='comony_url',
            new_name='company_url',
        ),
    ]