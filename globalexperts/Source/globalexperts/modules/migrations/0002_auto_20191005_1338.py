# Generated by Django 2.2 on 2019-10-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumodules',
            name='module_code',
            field=models.CharField(max_length=20, verbose_name='Module Code'),
        ),
    ]
