# Generated by Django 2.2 on 2019-10-07 13:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade_master', '0008_auto_20191007_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms_staticcontent',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Content', null=True, verbose_name='Content'),
        ),
    ]
