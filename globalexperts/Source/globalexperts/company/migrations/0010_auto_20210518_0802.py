# Generated by Django 2.2 on 2021-05-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_auto_20210505_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_settings',
            name='withdrawurl',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marketing Video Url'),
        ),
    ]
