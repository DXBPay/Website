import django_tables2 as tables
from django_tables2.utils import A
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import django_filters
from django_filters import DateRangeFilter,DateFilter
from datetime import date
from django.db.models import Q
import itertools
from django.contrib.auth.models import User

from cryptotoken.models import TokenDetails,RoadMap,CurrencyDetails,TokenInformation

class RoadMapTable(tables.Table):
     
     BUTTON_TEMPLATE = """
        <a href="{% url 'cryptotoken:roademapdit' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
        
       <a href="{% url 'cryptotoken:roadmapdetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
    
     
     class Meta:
         model =  RoadMap
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example1'}
         fields=['counter','title','years','status']


class TokenInformationTable(tables.Table):
     
     BUTTON_TEMPLATE = """
        <a href="{% url 'cryptotoken:tokenedit' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
        
       <a href="{% url 'cryptotoken:tokendetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
    
     
     class Meta:
         model =  TokenInformation
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example1'}
         fields=['counter','name','percentage','colour','status']


class CurrencyDetailsTable(tables.Table):
     
     BUTTON_TEMPLATE = """
        <a href="{% url 'cryptotoken:currencyedit' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
        
       
     
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
    
     
     class Meta:
         model =  CurrencyDetails
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example1'}
         fields=['counter','name','symbol','timerdate','attachments']


