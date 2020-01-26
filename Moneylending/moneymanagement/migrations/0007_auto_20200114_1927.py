# Generated by Django 2.2.7 on 2020-01-14 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moneymanagement', '0006_countries'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='countryName',
            new_name='country_Name',
        ),
        migrations.RemoveField(
            model_name='countries',
            name='countryID',
        ),
        migrations.AddField(
            model_name='countries',
            name='country_code',
            field=models.TextField(default='', max_length=30),
            preserve_default=False,
        ),
    ]