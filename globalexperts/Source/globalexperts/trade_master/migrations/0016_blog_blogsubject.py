# Generated by Django 2.2 on 2021-06-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_master', '0015_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blogsubject',
            field=models.TextField(blank=True, default='', help_text='Blogsubject', null=True, verbose_name='Blog subject'),
        ),
    ]
