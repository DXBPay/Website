# Generated by Django 2.2 on 2019-10-07 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade_master', '0005_auto_20191007_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='read_status',
            field=models.IntegerField(choices=[(0, 'UnReply'), (1, 'Replied')], default=0, verbose_name='Read Status'),
        ),
    ]
