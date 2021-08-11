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

Address_Status = (
		(0,'Active'),
		(1,'Inactive'),
		(2,'Cancelled')
	)
class UserAddress(models.Model):
	useraddress = models.CharField(max_length=100,verbose_name='Address')
	contractid=models.IntegerField(verbose_name='Contract ID',default=0)
	status=models.IntegerField(choices=Address_Status,default=0,verbose_name='Status')
	created_on = models.DateTimeField(auto_now_add = True)

	def __int__self(self):
		return id
	class Meta:
		verbose_name = 'Useraddress'
		db_table ='APLegJVs5IOqnDex'





