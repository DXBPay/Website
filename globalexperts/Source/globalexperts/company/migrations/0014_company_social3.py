# Generated by Django 2.2 on 2021-05-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_auto_20210527_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='social3',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Reddit'),
        ),
    ]