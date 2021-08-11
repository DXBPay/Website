from django.db import models
from django.conf import settings


from datetime import date
from django.contrib.auth.models import User,Group
from django.core.validators import RegexValidator
from auditable.models import Auditable

from django.urls import reverse
import os
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg ,F,DecimalField
from decimal import Decimal
import time

General_Status = (
					(0,'Active'),
					(1,'Inactive'),
					(2,'Cancel'),
	)
TICKET_Status = (
					(0,'Open'),
					(1,'Processing'),
					(2,'Closed'),
	)

Newsleter_Status = (
					(0,'All User'),
					(1,'Registered User'),
					(2,'Subscriber User'),
					(3,'Specific User'),
	)

class SupportCategory(Auditable):
	
	name = models.CharField(max_length=50,verbose_name='Category Name')
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __str__(self):
		return self.name
	class Meta:
		verbose_name='SupportCategory'
		db_table='Ww7tRv26SA7LAiQF'

class SupportTicket(Auditable):
	user = models.ForeignKey(User,related_name ='support_user_profile',on_delete=models.CASCADE)
	category = models.ForeignKey(SupportCategory,related_name ='support_categorylist',on_delete=models.CASCADE)
	subject = models.CharField(max_length=150,verbose_name='Subject')
	message = models.TextField(help_text='Message',verbose_name='Message',blank=True,null=True)
	attachment=models.ImageField(upload_to='usersupport',verbose_name='Attachements',blank=True,null=True)
	status=models.IntegerField(choices=TICKET_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id		
	class Meta:
		verbose_name='SupportTicket'
		db_table='TH3qkdA9J3URDVHw'
class SupportTicketDetails(Auditable):
	user = models.ForeignKey(User,related_name ='supportdetail_user_profile',on_delete=models.CASCADE)
	ticket = models.ForeignKey(SupportTicket,related_name ='support_ticketlist',on_delete=models.CASCADE)
	message = models.TextField(help_text='Message',verbose_name='Reply')
	attachment=models.ImageField(upload_to='usersupportdetail',verbose_name='Attachements',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id		
	class Meta:
		verbose_name='SupportTicketDetails'
		db_table='MBA4H1rKHZhDfggS'


class SubscribeUser(models.Model):
	user = models.ForeignKey(User,related_name ='subscribe_user_profile',on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add = True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id	
	class Meta:
		verbose_name='SubscribeUser'
		db_table='qdGChrivvbABICCF'	


class Newsletter(Auditable):
	user = models.ManyToManyField(User,related_name ='newsleter_user_profile')
	category = models.IntegerField(choices=Newsleter_Status,default=0,verbose_name='Type')
	subject = models.CharField(max_length=150,verbose_name='Subject')
	message = models.TextField(help_text='Message',verbose_name='Message',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id		
	class Meta:
		verbose_name='Newsletter'
		db_table='DbNwYgfcQ4osKvrl'	

class NewsletterSubscribeUser(models.Model):
	email = models.CharField(max_length=100,verbose_name='Email')
	created_on = models.DateTimeField(auto_now_add = True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name='NewsletterSubscribeUser'
		db_table='0CiKyhb05gCOp4mB'	