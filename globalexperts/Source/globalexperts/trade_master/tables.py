import django_tables2 as tables
from django_tables2.utils import A

from datetime import date
from django.db.models import Q

from django.contrib.auth.models import User


from trade_master.models import Cms_StaticContent,Faq,Contactus,EmailTemplate,Blog,Marketingvideo
from trade_master.models import Testimonial


class StaticContentTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       
        <a href="{% url 'trade_master:cms_page' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
      
       <a href="{% url 'trade_master:cms_page_detail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
     class Meta:
         model =  Cms_StaticContent
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','title','Actions']

class CmsContentTable(tables.Table):
     
     BUTTON_TEMPLATE = """
     
      <a href="{% url 'trade_master:cms_content' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
       
      <a href="{% url 'trade_master:cms_page_contentdetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
     class Meta:
         model =  Cms_StaticContent
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','title','Actions']

class BlogTable(tables.Table):
  BUTTON_TEMPLATE = """
     <a href="{% url 'trade_master:blog_page' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
      <a href="{% url 'trade_master:blog_detail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     """
  Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
  def render_counter(self, record):
    records = list(self.data)
    index = records.index(record)
    counter = index + 1
    return counter
    counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
  class Meta:
    model =  Blog
    orderable = True
    attrs = {'class': 'table table-bordered table-striped','id':'example2'}
    fields=['counter','blogtitle','Actions']


class MarketingTable(tables.Table):
  BUTTON_TEMPLATE = """
     <a href="{% url 'trade_master:video_page' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
     """
  Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
  def render_counter(self, record):
    records = list(self.data)
    index = records.index(record)
    counter = index + 1
    return counter
    counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
  class Meta:
    model =  Marketingvideo
    orderable = True
    attrs = {'class': 'table table-bordered table-striped','id':'example2'}
    fields=['counter','videotitle']



class TestimonialTable(tables.Table):
     
     BUTTON_TEMPLATE = """
      
        <a href="{% url 'trade_master:updatetestimonial' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
      
       
       <a href="{% url 'trade_master:testimonialdetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
     class Meta:
         model =  Testimonial
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','name','location','status','Actions']




class FaqTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       
        <a href="{% url 'trade_master:updatefaq' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
       
      
       
       <a href="{% url 'trade_master:detail_faq' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
     class Meta:
         model =  Faq
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','title','content','status','Actions']


class ContactusTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       
       {% if record.read_status == 0 %}
        <a href="{% url 'trade_master:contactus_update' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
      
        {% endif %}
       <a href="{% url 'trade_master:contactusdetail' record.id %}" title="Detail" class="btn"><i class="fa fa-info"></i></a>
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',) 
     class Meta:
         model =  Contactus
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','name','email','subject','read_status','created_on','modified_on','Actions']

class EmailTemplateTable(tables.Table):
     
     BUTTON_TEMPLATE = """
       
   
        <a href="{% url 'trade_master:updateemailcontent' record.id %}" title="Edit" class="btn"><i class="fa fa-edit"></i></a>
      
     """
     Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
     def render_counter(self, record):
      records = list(self.data)
      index = records.index(record)
      counter = index + 1
      return counter
     counter = tables.Column(verbose_name='S.No',orderable=False,accessor='pk',)
     class Meta:
         model =  EmailTemplate
         orderable = True
         attrs = {'class': 'table table-bordered table-striped','id':'example2'}
         fields=['counter','name','Subject','Actions']