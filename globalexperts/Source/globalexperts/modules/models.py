from django.db import models

from django.conf import settings


from datetime import date

from django.core.validators import RegexValidator


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

class MenuModules(models.Model):
	module_code =models.CharField(max_length=20,verbose_name='Module Code')
	module_name = models.CharField(max_length=50,verbose_name='Module Name')
	status=models.IntegerField(choices=General_Status,default=0,verbose_name='Status')

	def __int__self(self):
		return id
	class Meta:
		verbose_name = 'MenuModules'
		db_table='8yHbadiSPqTR4E0L'
	