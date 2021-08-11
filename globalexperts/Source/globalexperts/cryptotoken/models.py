from django.db import models

from django.conf import settings


from datetime import date

from django.core.validators import RegexValidator
from auditable.models import Auditable

from django.urls import reverse
import os
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg ,F,DecimalField
from decimal import Decimal
import time
import uuid
from ckeditor.fields import RichTextField
from django.utils import timezone
General_Status = (
					(0,'Active'),
					(1,'Inactive'),
					(2,'Cancel'),
	)
Liquidity_Lock = (
					(0,'UnLock'),
					(1,'Lock')
	)
class TokenDetails(Auditable):
	name = models.CharField(max_length=50,verbose_name='Name')
	symbol = models.CharField(max_length=50,verbose_name='Symbol')
	platform= models.CharField(max_length=50,verbose_name='Platform')
	supply=models.CharField(max_length=50,verbose_name='Total Supply',blank=True,null=True)
	teamwallet=models.CharField(max_length=50,verbose_name='Total Wallet',blank=True,null=True)
	presupply =models.CharField(max_length=50,verbose_name='Pre-Sale Supply ',blank=True,null=True)
	liquidtypool=models.CharField(max_length=50,verbose_name='Liquidity Pool',blank=True,null=True)
	token_burn =models.CharField(max_length=50,verbose_name='Token Burn',blank=True,null=True)
	presaleprice =models.CharField(max_length=50,verbose_name='Dx Sale Pre-Sale Price',blank=True,null=True)
	pancakeswap=models.CharField(max_length=50,verbose_name='PancakeSwap Price',blank=True,null=True)
	liquidity_lock = models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	content = models.TextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	def __str__(self):
		return "%s" % self.name

	class Meta:
		db_table='dT55INJGxASL7ISW'
		ordering = ['id']
		verbose_name = "TokenDetails"
		verbose_name_plural ="TokenDetails"
		indexes = [
			models.Index(fields=['name','symbol','status'])
		]


class RoadMap(Auditable):
	title = models.CharField(max_length=50,verbose_name='Title')
	years = models.CharField(max_length=50,verbose_name='Years')
	content = models.TextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	def __str__(self):
		return "%s" % self.title

	class Meta:
		db_table='cPWZ2sKnkhxQPL4c'
		ordering = ['id']
		verbose_name = "RoadMap"
		verbose_name_plural ="RoadMaps"
		indexes = [
			models.Index(fields=['title','years','status'])
		]


class CurrencyDetails(Auditable):
	name = models.CharField(max_length=50,verbose_name='Name')
	symbol = models.CharField(max_length=50,verbose_name='Symbol')
	platform= models.CharField(max_length=50,verbose_name='Platform')
	supply=models.CharField(max_length=50,verbose_name='Total Supply')
	reward_distributed =models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Distributor Holder (%)',default=0.0)
	charity =models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Charity Wallet (%)',default=0.0)
	marketing =models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Marketing Wallet (%)',default=0.0)
	teamwallet=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Team Wallet (%)',default=0.0)
	teamwallet_duration= models.IntegerField(verbose_name='Team Wallet Duration',default=0)
	presupply =models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Pre-Sale Supply (%) (DxSale)',default=0.0)
	liquidtypool=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Liquidity Pool (%) (PancakeSwap)',default=0.0)
	presaleprice =models.CharField(max_length=50,verbose_name='Dx Sale Pre-Sale Price',blank=True,null=True)
	pancakeswap=models.CharField(max_length=50,verbose_name='PancakeSwap Price',blank=True,null=True)
	token_burn =models.DecimalField(max_digits=8,decimal_places=2,verbose_name='Token Burn (%)',default=0.0)
	blackholeaddress = models.CharField(max_length=100,verbose_name='Hole Address',blank=True,null=True)
	liquiditylock = models.IntegerField(choices=Liquidity_Lock,default=0,verbose_name='Liquidity Lock')
	content = models.TextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	attachments = models.FileField(upload_to='currencywhitepaper',verbose_name='WhitePaper',blank=True,null=True)
	timerdate = models.DateTimeField(default=timezone.now,blank=True,null=True,verbose_name='Date')
	def __str__(self):
		return "%s" % self.name

	class Meta:
		db_table='fVqNkSDHT1M6Z0D6'
		ordering = ['id']
		verbose_name = "CurrencyDetails"
		verbose_name_plural ="CurrencyDetails"
		indexes = [
			models.Index(fields=['name','symbol','status'])
		]



class TokenInformation(Auditable):
	name = models.CharField(max_length=50,verbose_name='Name')
	percentage = models.CharField(max_length=50,verbose_name='Percentage')
	colour= models.CharField(max_length=50,verbose_name='Colour',blank=True,null=True)
	content = models.TextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	def __str__(self):
		return "%s" % self.name

	class Meta:
		db_table='kGR7rx1syW59TxKz'
		ordering = ['id']
		verbose_name = "TokenInformation"
		verbose_name_plural ="TokenInformation"
		indexes = [
			models.Index(fields=['name','percentage','status'])
		]