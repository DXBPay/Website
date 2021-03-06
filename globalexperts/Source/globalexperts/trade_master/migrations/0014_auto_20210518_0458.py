# Generated by Django 2.2 on 2021-05-18 04:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_master', '0013_subscribeuser_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Content', null=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='location',
            field=models.CharField(max_length=50, verbose_name='Position'),
        ),
    ]
