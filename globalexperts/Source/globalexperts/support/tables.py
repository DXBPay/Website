import django_tables2 as tables
from django_tables2.utils import A

from datetime import date
from django.db.models import Q

from django.contrib.auth.models import User


from support.models import SupportCategory,SupportTicket,Newsletter,SubscribeUser




class SupportCategoryTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       {% if menu_permissions_ticket == 1 %}
        <a href="{% url 'support:updatesupportcategory' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
       {% elif menu_permissions_ticket == 2 %}
        <a href="#" title="Edit" class="btn" style="cursor:default;"><i class="fa fa-edit"></i></a>
       {% endif %}
      
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
     class Meta:
         model =  SupportCategory
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','name','status','Actions']



class SupportTicketTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       {% if menu_permissions_ticket == 1 %}
        <a href="{% url 'support:detail_supportticket' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
       {% elif menu_permissions_ticket == 2 %}
        <a href="#" title="Edit" class="btn" style="cursor:default;"><i class="fa fa-edit"></i></a>
       {% endif %}

      
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
     class Meta:
         model =  SupportTicket
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','user','user.email','category','subject','status','Actions']



class NewsletterTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       {% if menu_permissions_newsletter == 1 %}
        <a href="{% url 'support:newsletterdetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
       {% elif menu_permissions_newsletter == 2 %}
        <a href="#" title="Detail" class="btn" style="cursor:default;"><i class="fa fa-edit"></i></a>
       {% endif %}
      
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     
     class Meta:
         model =  Newsletter
         orderable = False
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['category','subject','Actions']

class SubscribeUserTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       {% if menu_permissions_ticket == 1 %}
        <a href="{% url 'support:newsletterdetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
       {% elif menu_permissions_ticket == 2 %}
        <a href="#" title="Detail" class="btn" style="cursor:default;"><i class="fa fa-edit"></i></a>
       {% endif %}
      
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     
     class Meta:
         model =  SubscribeUser
         orderable = False
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['user','subject','Actions']