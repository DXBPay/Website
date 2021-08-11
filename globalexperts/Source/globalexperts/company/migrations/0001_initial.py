# Generated by Django 2.2 on 2019-10-01 16:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='CompanyName', max_length=50, verbose_name='Site Name')),
                ('caption', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Site Caption')),
                ('director', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Director')),
                ('reg_info', models.CharField(blank=True, default='', max_length=60, null=True, verbose_name='Site Registration Info')),
                ('address1', models.CharField(max_length=100, verbose_name='Contact Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('postcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Pin Code')),
                ('phone1', models.CharField(blank=True, help_text='Phone number Format : 0xxxxxxxxxx', max_length=13, null=True, verbose_name='Phone Number')),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=60, null=True)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='logo', verbose_name='Site Logo')),
                ('company_fav', models.ImageField(blank=True, null=True, upload_to='favicons', verbose_name='Site Favicon')),
                ('copy_right', models.CharField(blank=True, max_length=200, null=True, verbose_name='Copy Rights')),
                ('admin_redirect', models.CharField(blank=True, max_length=100, null=True, verbose_name='Admin Redirect')),
                ('trade_percentage', models.DecimalField(decimal_places=8, default='0.00000000', max_digits=16, verbose_name='Trade Percentage')),
                ('gplus', models.CharField(blank=True, max_length=200, null=True, verbose_name='Google Plus')),
                ('fb', models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter')),
                ('linkedin', models.CharField(blank=True, max_length=200, null=True, verbose_name='LinkedIn')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='Instagram')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='Company_Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_maintenance_status', models.IntegerField(choices=[(0, 'Enable'), (1, 'Disable')], default=1, verbose_name='Site Maintenance')),
                ('site_maintenance', models.TextField(blank=True, null=True)),
                ('new_coin_status', models.IntegerField(choices=[(0, 'Enable'), (1, 'Disable')], default=1, verbose_name='Fees Status')),
                ('fees_amount', models.DecimalField(decimal_places=8, default='0.00000000', max_digits=16, verbose_name='Fee Amount')),
                ('free_bonus_status', models.IntegerField(choices=[(0, 'Enable'), (1, 'Disable')], default=1, verbose_name='Bonus Provide Status')),
                ('bonus_amount', models.DecimalField(decimal_places=8, default='0.00000000', max_digits=16, verbose_name='Bonus Amount')),
                ('free_days', models.CharField(blank=True, default='Free days', max_length=10, null=True)),
                ('margin_percentage', models.DecimalField(decimal_places=8, default='0.00000000', max_digits=16, verbose_name='Margin Percentage')),
                ('lending_percentage', models.DecimalField(decimal_places=8, default='0.00000000', max_digits=16, verbose_name='Lending Percentage')),
                ('base_price_percenatge', models.DecimalField(decimal_places=8, default='0.00000000', max_digits=16, verbose_name='Base Price Percentage')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('company_settings_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='company_settings', to='company.Company')),
            ],
            options={
                'verbose_name': 'CompanySetting',
                'verbose_name_plural': 'CompanySetting',
            },
        ),
        migrations.CreateModel(
            name='Company_Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='BranchName', max_length=50, verbose_name='Branch Name')),
                ('address1', models.CharField(max_length=100, verbose_name='Contact Address')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('postcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Pin Code')),
                ('phone1', models.CharField(blank=True, help_text='Phone number Format : 0xxxxxxxxxx', max_length=13, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 13 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=60, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='company.Company')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
