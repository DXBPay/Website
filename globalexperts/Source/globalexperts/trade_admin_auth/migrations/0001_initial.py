# Generated by Django 2.2 on 2021-05-03 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0006_auto_20201228_1927'),
        ('modules', '0003_auto_20201228_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('for_trade', models.BooleanField(default=False)),
                ('for_twofactor', models.BooleanField(default=False)),
                ('for_changepassword', models.BooleanField(default=False)),
                ('for_newdevices', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification_modified_by_user', to=settings.AUTH_USER_MODEL)),
                ('user_notificatio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User_Notification',
                'db_table': 'IYfug8IDJJMTbu1H',
            },
        ),
        migrations.CreateModel(
            name='User_Kyc_Verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='user_frontimage', verbose_name='Front Image Proof')),
                ('front_reason', models.TextField(blank=True, null=True, verbose_name='Front Proof Reason')),
                ('back_image', models.ImageField(blank=True, null=True, upload_to='user_backimage', verbose_name='Back Image Proof')),
                ('back_image_status', models.BooleanField(default=False)),
                ('back_reason', models.TextField(blank=True, null=True, verbose_name='Bacl Proof Reason')),
                ('selfie_image', models.ImageField(blank=True, null=True, upload_to='user_selfieimage', verbose_name='Selfie Image Proof')),
                ('selfie_reason', models.TextField(blank=True, null=True, verbose_name='Bacl Proof Reason')),
                ('front_image_status_update', models.IntegerField(choices=[(0, 'Not verified'), (1, 'Pending'), (2, 'Verified'), (3, 'Rejected')], default=0, verbose_name='Front Image Status')),
                ('back_image_status_update', models.IntegerField(choices=[(0, 'Not verified'), (1, 'Pending'), (2, 'Verified'), (3, 'Rejected')], default=0, verbose_name='Back Image Status')),
                ('selfie_image_status_update', models.IntegerField(choices=[(0, 'Not verified'), (1, 'Pending'), (2, 'Verified'), (3, 'Rejected')], default=0, verbose_name='Selfie Image Status')),
                ('kyc_status', models.IntegerField(choices=[(0, 'Not verified'), (1, 'Pending'), (2, 'Verified'), (3, 'Rejected')], default=0, verbose_name='KYC Status')),
                ('prooftype', models.IntegerField(choices=[(0, 'Aadhaar Card'), (1, 'Passport'), (2, 'Pan Card'), (3, 'Driving Lience'), (4, 'Voter ID')], default=0, verbose_name='Proof Type')),
                ('proofid', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Number')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kyc_verification_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kyc_verification_modified_by_user', to=settings.AUTH_USER_MODEL)),
                ('user_kyc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kycverification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User KYCVerification',
                'verbose_name_plural': "User KYCVerification's",
                'db_table': 'FS5ywpeqlFDMswG7',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='MenuPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('access_permissions', models.IntegerField(blank=True, choices=[(0, 'NotAssign'), (1, 'Write'), (2, 'Read')], null=True, verbose_name='Access Permissions')),
                ('access_modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modules.MenuModules')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menupermissions_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menupermissions_modified_by_user', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user_menupermissions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MenuPermissions',
                'db_table': '1Cs8VH6oGW3Zh7F0',
            },
        ),
        migrations.CreateModel(
            name='AdminUser_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(blank=True, choices=[(0, 'Male'), (1, 'Female')], null=True, verbose_name='Gender')),
                ('date_of_birth', models.DateField(blank=True, help_text='Date of Birth in mm/dd/yyyy Format', null=True)),
                ('address1', models.CharField(max_length=100, verbose_name='Contact Address1')),
                ('address2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Contact Address2')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('postcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='Pin Code')),
                ('phone1', models.CharField(blank=True, max_length=13, null=True, verbose_name='Phone Number')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='tradeuserprofile', verbose_name='Profile Picture')),
                ('role', models.IntegerField(choices=[(0, 'Admin'), (1, 'SubAdmin'), (2, 'Tradeusers')], default=0, verbose_name='Role')),
                ('pattern_code', models.IntegerField(default=0, verbose_name='Pattern Code')),
                ('country_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Country Code')),
                ('twofa', models.BooleanField(default=False)),
                ('google_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='Google Id')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active'), (2, 'Deactive'), (3, 'Cancelled')], default=0, verbose_name='Status')),
                ('referal_status', models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0, verbose_name='Referal Status')),
                ('referal_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='Referal Code')),
                ('referal_by_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='ReferalBy Code')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_user_country', to='locations.Country', verbose_name='Country')),
                ('referal_user_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_referalby', to=settings.AUTH_USER_MODEL, verbose_name='Refered User')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': "User Profile's",
                'db_table': 'O8eIUL1BZ1szt93p',
            },
        ),
        migrations.CreateModel(
            name='AdminUser_Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('activity', models.CharField(blank=True, max_length=50, null=True, verbose_name='Activity')),
                ('browsername', models.CharField(blank=True, max_length=50, null=True, verbose_name='Browser Name')),
                ('os', models.CharField(blank=True, max_length=50, null=True, verbose_name='Operating System')),
                ('devices', models.CharField(blank=True, max_length=50, null=True, verbose_name='Devices')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminuser_activity_created_by_user', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adminuser_activity_modified_by_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_user_activity', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AdminUser_Activity',
                'db_table': '3Ot7bXB6FqYeKBcT',
            },
        ),
        migrations.AddIndex(
            model_name='user_kyc_verification',
            index=models.Index(fields=['user_kyc', 'kyc_status'], name='FS5ywpeqlFD_user_ky_459984_idx'),
        ),
        migrations.AddIndex(
            model_name='adminuser_profile',
            index=models.Index(fields=['gender', 'twofa', 'status'], name='O8eIUL1BZ1s_gender_a1a152_idx'),
        ),
    ]
