# Generated by Django 2.2 on 2019-10-05 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms_staticcontent',
            name='content',
            field=models.TextField(blank=True, help_text='Content', null=True, verbose_name='Content'),
        ),
    ]
