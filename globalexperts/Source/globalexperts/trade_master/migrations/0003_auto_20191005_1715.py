# Generated by Django 2.2 on 2019-10-05 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_master', '0002_auto_20191005_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cms_staticcontent',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='Question')),
                ('content', models.TextField(blank=True, help_text='Content', null=True, verbose_name='Content')),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive'), (2, 'Cancel')], default=0, verbose_name='Status')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faq_modified_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]