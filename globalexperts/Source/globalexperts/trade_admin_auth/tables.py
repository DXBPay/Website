import django_tables2 as tables
from django_tables2.utils import A
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import django_filters
from django_filters import DateRangeFilter,DateFilter
from django import forms
from datetime import date
from django.db.models import Q
import itertools

from django.contrib.auth.models import User


from trade_admin_auth.models import AdminUser_Profile,AdminUser_Activity

from trade_auth.models import UserAddress
def next_count():
    return next(counter)

class UserAddressTable(tables.Table):
    
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
     class Meta:
         model =  UserAddress
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','useraddress','created_on']


