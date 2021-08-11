# Generated by Django 2.2 on 2020-07-16 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0007_auto_20200706_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportticket',
            name='status',
            field=models.IntegerField(choices=[(0, 'Open'), (1, 'Processing'), (2, 'Closed')], default=0, verbose_name='Status'),
        ),
        migrations.CreateModel(
            name='SupportTicketDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(help_text='Message', verbose_name='Reply')),
                ('attachment', models.ImageField(blank=True, null=True, upload_to='usersupportdetail', verbose_name='Attachements')),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive'), (2, 'Cancel')], default=0, verbose_name='Status')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supportticketdetails_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supportticketdetails_modified_by_user', to=settings.AUTH_USER_MODEL)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_ticketlist', to='support.SupportTicket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supportdetail_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]