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

from ckeditor.fields import RichTextField


General_Status = (
					(0,'Active'),
					(1,'Inactive'),
					(2,'Cancel'),
	)
Content_type = (
	(0,'page'),
	(1,'content')

	)
Read_Status = (
	(0,'UnReply'),
	(1,'Replied')
	)

class Cms_StaticContent(Auditable):
	name = models.CharField(max_length=50,verbose_name='Name',blank=True,null=True)
	title = models.CharField(max_length=50,verbose_name='Title')
	content = RichTextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	contenttype=models.IntegerField(choices=Content_type,default=0,verbose_name='Content')
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name='Cms_StaticContent'
		db_table='ax7XI2mneaLpb7Ud'


class Faq(Auditable):
	
	title = models.CharField(max_length=50,verbose_name='Question')
	content = models.TextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name='Faq'
		db_table='gAoTkpN4b2jBB6tV'


class Contactus(models.Model):

	phone1=models.CharField(max_length=13,verbose_name='Phone Number',blank=True,null=True)
	name =models.CharField(max_length=50,verbose_name='Name')
	email = models.CharField(max_length=50,verbose_name='Email')
	subject = models.CharField(max_length=50,verbose_name='Subject')
	message = models.TextField(help_text='Message',verbose_name='Message')
	reply = models.TextField(help_text='Message',verbose_name='Reply',blank=True,null=True)
	status =models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	read_status =models.IntegerField(choices=Read_Status,default=0,verbose_name='Read Status')
	created_on = models.DateTimeField(auto_now_add = True)
	modified_on = models.DateTimeField(auto_now=True)

	def __int__self(self):
		return id
	class Meta:
		verbose_name='Contactus'
		db_table='tg3bHbh1qpLYMIaS'


class EmailTemplate(Auditable):
	
	name = models.CharField(max_length=50,verbose_name='Name')
	Subject = models.CharField(max_length=300,verbose_name='Subject')
	content = RichTextField(help_text='Content',verbose_name='Content')
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name='EmailTemplate'
		db_table='rfkF0iB1AluS2NNQ'


class Testimonial(Auditable):
	name = models.CharField(max_length=50,verbose_name='Name')
	location = models.CharField(max_length=50,verbose_name='Position')
	content = RichTextField(help_text='Content',verbose_name='Content',blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')
	photo=models.ImageField(upload_to='testimonialimages',verbose_name='Photo',blank=True,null=True)
	def __int__self(self):
		return id
	class Meta:
		verbose_name='Testimonial'
		db_table='DC1MIHelrUsOiies'


class Subscribeuser(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	emailaddress = models.CharField(max_length=50)
	subscribe_status = models.CharField(max_length=50)
	class Meta:
		db_table = 'Z0EDN1feYgvqc7eB'


class Newsletter(models.Model):
	ty = (
		('All user','All user'),
		('Registered user','Registered user'),
		('Subscribed user','Subscribed user'),
	)
	Type = models.CharField(max_length=50,choices=ty,default="")
	email = models.CharField(max_length=50)
	subj = models.CharField(max_length=50)
	message = models.TextField()
	class Meta:
		db_table = 'TfFGdWoiaPvleABv'



class Blog(Auditable):
	blogtitle = models.CharField(max_length=100,verbose_name='Blog Name')
	blogimage = models.ImageField(upload_to='Blogimage',null=True,blank=True)
	blogcontent = RichTextField(help_text='Blogcontent',verbose_name='Blog Content',null=True,blank=True)
	blogsubject = models.TextField(help_text='Blogsubject',verbose_name='Blog subject',blank=True,null=True,default="")
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name = 'Blog'
		db_table = 'H5gqo7sKYMKJmelh'



class Marketingvideo(Auditable):
	videotitle = models.CharField(max_length=100,verbose_name='Video Title')
	videourl = models.CharField(max_length=100,blank=True,null=True)
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name = 'Marketingvideo'
		db_table = 'Ywv5RGoHxejMoUV'