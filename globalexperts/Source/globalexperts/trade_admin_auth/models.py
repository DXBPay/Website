from django.db import models

from django.conf import settings

from django.contrib.auth.models import User,Group

from auditable.models import Auditable

from datetime import date

from django.core.validators import RegexValidator
import uuid
import os

from django.urls import reverse
import os
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg ,F,DecimalField
from decimal import Decimal
import time

from locations.models import Country,State,Cities

from modules.models import MenuModules


User_Role = (
		(0,'Admin'),
		(1,'SubAdmin'),
		(2,'Tradeusers')
	)
User_Status =(
		(0,'Inactive'),
		(1,'Active'),
		(2,'Deactive'),
		(3,'Cancelled')
	)
Permission_Access =(
	(0,'NotAssign'),
	(1,'Write'),
	(2,'Read'),
	)
Gender = (

	(0,'Male'),
	(1,'Female'),
	)
KYC_List =(

	(0,'Aadhaar Card'),
	(1,'Passport'),
	(2,'Pan Card'),
	(3,'Driving Lience'),
	(4,'Voter ID'),
	
	)
Kyc_verification_Status =(
	(0,'Not verified'),
	(1,'Pending'),
	(2,'Verified'),
	(3,'Rejected'),
	)
Referal_Status = (
		(0,'No'),
		(1,'Yes'),
	)

class AdminUser_Profile(models.Model):
	user = models.OneToOneField(User,related_name ='admin_user_profile',on_delete=models.CASCADE)
	gender = models.IntegerField(choices=Gender,verbose_name='Gender',blank=True,null=True)
	date_of_birth = models.DateField(help_text='Date of Birth in mm/dd/yyyy Format',blank=True,null=True)

	address1 = models.CharField(max_length=100,verbose_name='Contact Address1')
	address2 = models.CharField(max_length=100,verbose_name='Contact Address2',blank=True,null=True)
	city = models.CharField(max_length=30,verbose_name='City',blank=True,null=True)
	state = models.CharField(max_length=50,verbose_name='State',blank=True,null=True)
	country = models.ForeignKey(Country,related_name ='admin_user_country',on_delete=models.CASCADE,verbose_name='Country',blank=True,null=True)
	postcode = models.CharField(max_length=10,verbose_name='Pin Code',blank=True,null=True)
	phone1 = models.CharField(max_length=13,verbose_name='Phone Number',blank=True,null=True)
	photo = models.ImageField(upload_to='tradeuserprofile',verbose_name='Profile Picture',blank=True,null=True)
	role = models.IntegerField(choices=User_Role,default=0,verbose_name='Role')
	pattern_code = models.IntegerField(verbose_name='Pattern Code',default=0)
	country_code = models.CharField(max_length=10,verbose_name='Country Code',blank=True,null=True)
	twofa = models.BooleanField(default=False)
	google_id = models.CharField(max_length=20,verbose_name='Google Id',blank=True,null=True)
	status = models.IntegerField(choices=User_Status,default=0,verbose_name = 'Status')
	referal_status = models.IntegerField(choices=Referal_Status,default=0,verbose_name = 'Referal Status')
	referal_code = models.CharField(max_length=10,verbose_name='Referal Code',blank=True,null=True)
	referal_user_by = models.ForeignKey(User,related_name ='user_referalby',on_delete=models.CASCADE,verbose_name='Refered User',blank=True,null=True)
	referal_by_code =  models.CharField(max_length=10,verbose_name='ReferalBy Code',blank=True,null=True)
	emailaddress = models.CharField(max_length=100,verbose_name='Email Address',blank=True,null=True)
	def __str__(self):
		return "%s's profile" % self.user
	@property
	def image_name(self):
		return  os.path.basename(self.photo.path) if self.photo else ''
	

	def referalcount(self):
		Referal_Count = 0
		referal_details = AdminUser_Profile.objects.filter(Q(status=0) & Q(referal_user_by =self.user.id )).order_by('id')
		Referal_Count = referal_details.count()
		return	Referal_Count
	def kycstatus(self):
		Plan_Count = 0
		kycstatus = User_Kyc_Verification.objects.get(Q(user_kyc =self.user.id ))
		kyc_status = kycstatus.kyc_status
		
		return	kyc_status
	class Meta:
		db_table='O8eIUL1BZ1szt93p'
		verbose_name = "User Profile"
		verbose_name_plural ="User Profile's"
		indexes = [
		models.Index(fields=['gender','twofa','status'])

		]


class AdminUser_Activity(Auditable):
	user = models.ForeignKey(User,related_name ='admin_user_activity',on_delete=models.CASCADE)
	ip_address = models.GenericIPAddressField()
	activity=models.CharField(max_length=50,verbose_name='Activity',blank=True,null=True)
	browsername = models.CharField(max_length=50,verbose_name='Browser Name',blank=True,null=True)
	os=models.CharField(max_length=50,verbose_name='Operating System',blank=True,null=True)
	devices=models.CharField(max_length=50,verbose_name='Devices',blank=True,null=True)

	def __int__self(self):
		return id
	class Meta:
		verbose_name ='AdminUser_Activity'
		db_table='3Ot7bXB6FqYeKBcT'	
class MenuPermissions(Auditable):
	user_permissions = models.ForeignKey(User,related_name ='admin_user_menupermissions',on_delete=models.CASCADE)
	access_modules = models.ForeignKey(MenuModules,on_delete=models.CASCADE)
	access_permissions=models.IntegerField(choices=Permission_Access,verbose_name='Access Permissions',blank=True,null=True)

	def __int__self(self):
		return id
	class Meta:
		verbose_name ='MenuPermissions'
		db_table='1Cs8VH6oGW3Zh7F0'

class User_Notification(Auditable):
	user_notificatio = models.ForeignKey(User,related_name ='user_notification',on_delete=models.CASCADE)
	
	for_trade = models.BooleanField(default=False)
	for_twofactor = models.BooleanField(default=False)
	for_changepassword = models.BooleanField(default=False)
	for_newdevices = models.BooleanField(default=False)

	def __int__self(self):
		return id
	class Meta:
		verbose_name ='User_Notification'
		db_table='IYfug8IDJJMTbu1H'

class User_Kyc_Verification(Auditable):

	user_kyc =models.ForeignKey(User,related_name ='user_kycverification',on_delete=models.CASCADE)
	front_image = models.ImageField(upload_to='user_frontimage',verbose_name='Front Image Proof',blank=True,null=True)
	front_reason = models.TextField(verbose_name='Front Proof Reason' ,blank=True,null=True)
	back_image = models.ImageField(upload_to='user_backimage',verbose_name='Back Image Proof',blank=True,null=True)
	back_image_status = models.BooleanField(default=False)
	back_reason = models.TextField(verbose_name='Bacl Proof Reason' ,blank=True,null=True)
	selfie_image = models.ImageField(upload_to='user_selfieimage',verbose_name='Selfie Image Proof',blank=True,null=True)
	selfie_reason = models.TextField(verbose_name='Bacl Proof Reason' ,blank=True,null=True)
	front_image_status_update = models.IntegerField(choices=Kyc_verification_Status,default=0,verbose_name='Front Image Status')
	back_image_status_update = models.IntegerField(choices=Kyc_verification_Status,default=0,verbose_name='Back Image Status')
	selfie_image_status_update = models.IntegerField(choices=Kyc_verification_Status,default=0,verbose_name='Selfie Image Status')
	kyc_status = models.IntegerField(choices=Kyc_verification_Status,default=0,verbose_name='KYC Status')
	prooftype = models.IntegerField(choices=KYC_List,default=0,verbose_name='Proof Type')
	proofid = models.CharField(max_length=50,verbose_name='ID Number',blank=True,null=True)


	def __int__self(self):
		return id

	class Meta:
		ordering = ['-id']
		db_table='FS5ywpeqlFDMswG7'
		verbose_name = "User KYCVerification"
		verbose_name_plural ="User KYCVerification's"
		indexes = [
		models.Index(fields=['user_kyc','kyc_status'])

		]