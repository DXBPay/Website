# Generated by Django 2.2 on 2021-06-03 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0019_auto_20210603_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_settings',
            name='site_maintenance',
            field=models.TextField(blank=True, null=True, verbose_name='Coming Soon Message'),
        ),
    ]
