# Generated by Django 4.1.2 on 2022-10-22 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0005_rename_comony_url_author_company_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='genericpage',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='generic.author'),
        ),
    ]
