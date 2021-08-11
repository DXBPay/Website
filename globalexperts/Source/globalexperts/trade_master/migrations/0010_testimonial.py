# Generated by Django 2.2 on 2020-12-08 17:14

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trade_master', '0009_auto_20191007_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('content', ckeditor.fields.RichTextField(help_text='Content', verbose_name='Content')),
                ('status', models.IntegerField(choices=[(0, 'Active'), (1, 'Inactive'), (2, 'Cancel')], default=0, verbose_name='Status')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='testimonialimages', verbose_name='Photo')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonial_modified_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]