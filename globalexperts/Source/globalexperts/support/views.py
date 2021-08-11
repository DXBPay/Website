from django.shortcuts import render
from django.shortcuts import render,get_list_or_404, get_object_or_404
from django.conf import settings


from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic import TemplateView,View


from django.http.response import HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.urls import reverse
from django.urls import reverse_lazy
from django.template.context_processors import csrf
from django.shortcuts import redirect
from django.http import JsonResponse

from datetime import date,timedelta
import datetime
import json


from django.db.models import Q,F,Func,Value
from django.db.models import Count, Min,Max, Sum, Avg,DecimalField,DateTimeField,CharField
from django.db.models.expressions import RawSQL
from django.db.models.functions import Cast,TruncSecond,ExtractSecond


from django.db import transaction

from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.core.mail import send_mail

from trade_perms.mixins import OR_PermissionsRequiredMixin, shared_permission_access, admin_permission_access
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.core.exceptions import PermissionDenied
from auditable.views import AuditableMixin
from django.db.models import Subquery
# from trade_auth.views import count_referal_code
from trade_auth.views import CompanyMaintanceRequiredMixin,check_company

from django_ajax.decorators import ajax
from trade_admin_auth.mixins import check_group
from trade_admin_auth.mixins import ManageTicketSupportAdminRequiredMixin,ManageNewsletterAdminRequiredMixin

from django_tables2 import RequestConfig
from support.models import SupportCategory,SupportTicket,Newsletter,SubscribeUser,NewsletterSubscribeUser
from support.models import SupportTicketDetails
from support.forms import SupportCategoryForm,NewsletterForm,SupportTicketForm,SupportTicketDetailAdminForm
from support.forms import SupportTicketDetailForm
from support.tables import SupportCategoryTable,SupportTicketTable,NewsletterTable

from trade_master.models import EmailTemplate

import base64
import re
from Crypto.Cipher import AES

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import base64, json, math
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


class AddSupportCategory(ManageTicketSupportAdminRequiredMixin,CreateView):
    model = SupportCategory
    form_class = SupportCategoryForm
    template_name = 'support/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(AddSupportCategory, self).get_context_data(**kwargs)
       context['Title'] = 'Add SupportCategory'
       context['activecls']='supportadmin'
       context['Btn_url']='support:supportcategorylist'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'support category created successfully.')
       return HttpResponseRedirect('/support/supportcategorylist/')

class ListSupportCategory(ManageTicketSupportAdminRequiredMixin,ListView):
    model = SupportCategory
    template_name = 'support/generic_list_add.html'
    def get_queryset(self, **kwargs):
      return SupportCategory.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListSupportCategory, self).get_context_data(**kwargs)
        context['Title'] = 'List SupportCategory '
        content_qs = SupportCategory.objects.all()
        context['content_qs'] =content_qs
        contenttable = SupportCategoryTable(content_qs)
        context['table'] = contenttable
        context['add_title'] ='Add SupportCategory'
        context['Btn_url'] = 'support:addsupportcategory'
        context['activecls']='supportadmin'
        return context   

class UpdateSupportCategory(ManageTicketSupportAdminRequiredMixin,UpdateView):
    model = SupportCategory
    form_class = SupportCategoryForm
    template_name = 'support/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateSupportCategory, self).get_context_data(**kwargs)
       context['Title'] = 'Update SupportCategory'
       context['Btn_url']='support:supportcategorylist'
       context['activecls']='supportadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'support category updated successfully.')
       return HttpResponseRedirect('/support/supportcategorylist/')



class ListSupportTicket(ManageTicketSupportAdminRequiredMixin,ListView):
    model = SupportTicket
    template_name = 'support/generic_list.html'
    def get_queryset(self, **kwargs):
      return SupportTicket.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListSupportTicket, self).get_context_data(**kwargs)
        context['Title'] = 'List SupportTickets '
        content_qs = SupportTicket.objects.all()
        context['content_qs'] =content_qs
        contenttable = SupportTicketTable(content_qs)
        context['table'] = contenttable
        context['add_title'] ='Add SupportCategory'
        context['Btn_url'] = 'support:addsupportcategory'
        context['activecls']='supportadmin'
        return context   

class UpdateSupportTicket(ManageTicketSupportAdminRequiredMixin,UpdateView):
    model = SupportTicket
    form_class = SupportCategoryForm
    template_name = 'support/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateSupportTicket, self).get_context_data(**kwargs)
       context['Title'] = 'Update SupportTickets'
       context['activecls']='supportadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'support ticket updated successfully.')
       return HttpResponseRedirect('/support/ticketsupportlist/')

class DetailSupportticket(ManageTicketSupportAdminRequiredMixin,DetailView):
    model = SupportTicket 
    template_name = 'support/ticketdetail_detail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailSupportticket, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = SupportTicket.objects.get(id=p_key)
       context['Title'] = 'SupportTicket Detail'
       context['staticcontent_qs']=staticcontent_qs
       context['activecls']='supportadmin'
       
       return context         

class AddNewsletter(ManageNewsletterAdminRequiredMixin,CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'support/newsletter.html'   
    def get_context_data(self, **kwargs):
       context = super(AddNewsletter, self).get_context_data(**kwargs)
       context['Title'] = 'Add Newsletter'
       context['userlist'] = User.objects.filter(admin_user_profile__role=2)
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'newsletter created successfully.')
       return HttpResponseRedirect('/support/listnewsletter/')       

class ListNewsletter(ManageNewsletterAdminRequiredMixin,ListView):
    model = Newsletter
    template_name = 'support/generic_list_add.html'
    def get_queryset(self, **kwargs):
      return Newsletter.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListNewsletter, self).get_context_data(**kwargs)
        context['Title'] = 'List Newsletter '
        content_qs = Newsletter.objects.all()
        context['content_qs'] =content_qs
        contenttable = NewsletterTable(content_qs)
        context['table'] = contenttable
        context['add_title'] ='Add Newsletter'
        context['Btn_url'] = 'support:addnewsletter'
        return context

class DetailNewsletter(ManageNewsletterAdminRequiredMixin,DetailView):
    model = Newsletter 
    template_name = 'support/newsletterdetail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailNewsletter, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Newsletter.objects.get(id=p_key)
       context['Title'] = 'Newsletter Detail'
       context['staticcontent_qs']=staticcontent_qs
       return context                         


class ListSubscribeUserAdmin(ListView):
    model = NewsletterSubscribeUser
    template_name = 'support/subscribeuser_list.html'
    def get_queryset(self, **kwargs):
      return NewsletterSubscribeUser.objects.all().order_by('-id')
    
    def get_context_data(self,**kwargs):
        context=super(ListSubscribeUserAdmin, self).get_context_data(**kwargs)
        context['Title'] = 'Subscribe User List'
        tradeuser_qs = NewsletterSubscribeUser.objects.all().order_by('-id')
        context['subadmin_qs'] =tradeuser_qs
        context['activecls']='newsletteradmin'
        return context       


class DeleteSubscribeuser(View):
    def get(self, request, *args, **kwargs):
        pkey =  (self.kwargs['pk'])
        status = ''
        user_qs = get_object_or_404(NewsletterSubscribeUser, pk=pkey)
        if user_qs.status == 1:
            user_qs.status = 0
            status = 'activated'
        elif user_qs.status == 0:    
            user_qs.status = 1
            status = 'deactivated'
        user_qs.save()
        
        messages.add_message(request, messages.SUCCESS, 'SubscribeUser '+status+' status updated successfully.') 
        return HttpResponseRedirect(reverse('support:subscribelist'))


def subscribeuser(request):
  if request.method == 'POST':
    get_email = request.POST.get('email','')
    user_eail = NewsletterSubscribeUser.objects.filter(email=get_email)
    if user_eail.exists():
      messages.add_message(request,messages.ERROR,'You Already Subscribed')
      return HttpResponseRedirect("/")
    else:
      if get_email is not None and get_email != '':
        create_user_wallet = NewsletterSubscribeUser.objects.create(email=get_email,status=0,created_on=datetime.datetime.now(),)
        messages.add_message(request, messages.SUCCESS, 'newsletter subscription created successfully.')
        return HttpResponseRedirect('/')
      else:  
        messages.error(request,'Invalid email address')
        return HttpResponseRedirect('/')
  else:    
    messages.error(request,'Invalid email address')
    return HttpResponseRedirect('/')



class AddSupportView(CompanyMaintanceRequiredMixin,CreateView):
  model = SupportTicket
  form_class = SupportTicketForm
  template_name = 'support/supportform.html'
  
  def get_context_data(self, **kwargs):
    context = super(AddSupportView, self).get_context_data(**kwargs)
    context['Title'] = 'Support Ticket'
    context['keywords'] = 'Support Ticket,'
    context['content'] = 'Support Ticket is raise  failed transaction and information.'
    context['activecls']='support'
    try:
      supportdetail = SupportTicket.objects.filter(user=self.request.user.id)
    except SupportTicket.DoesNotExist:
      supportdetail = ''
    context['supportdetail'] =  supportdetail 
    userqueryset = SupportCategory.objects.filter(status=0)
    context['userqueryset'] = userqueryset
    return context

  @transaction.atomic
  def form_valid(self, form):
    form.instance.user_id = self.request.user.id
    form.instance.created_by_id = self.request.user.id
    form.instance.modified_by_id = self.request.user.id
    form.instance.status = 0
    formsave=form.save()
    messages.add_message(self.request, messages.SUCCESS, 'Support Ticket submitted successfully.')
    return HttpResponseRedirect(reverse('support:supportticket'))

@check_company('site')
def tradeusersupportreply_view(request,supportid):
    context={}
    try:
        support = SupportTicket.objects.get(id=supportid)
    except SupportTicket.DoesNotExist:
        support = ''
    try:
      supportdetail = SupportTicketDetails.objects.filter(user=request.user.id)
    except SupportTicketDetails.DoesNotExist:
      supportdetail = ''
    context['supportdetail'] =  supportdetail 
    if request.method == 'POST':

       form = SupportTicketDetailForm(request.POST, request.FILES)
       if form.is_valid():
          agree = form.cleaned_data['agree']
          
          updateagree = 0
          if agree == True:
            updateagree = 2
            
          elif agree == False:
            updateagree = 0
            
          form.instance.user_id = support.user.id
          form.instance.ticket_id = support.id
          form.instance.created_by_id  = request.user.id
          form.instance.created_on   = datetime.datetime.now()
          form.instance.modified_by = request.user
          form.instance.status = 0
          form.save()
          updatesupport = SupportTicket.objects.get(id=supportid)
          updatesupport.status = updateagree
          updatesupport.save()
          
          messages.add_message(request, messages.SUCCESS, 'Reply message submitted successfully.')
          return HttpResponseRedirect('/support/tradeuser_supportticket/'+str(supportid)+'/')
       else:
          messages.add_message(request, messages.ERROR, 'All field must required.')
          return HttpResponseRedirect('/support/tradeuser_supportticket/'+str(supportid)+'/')
       
       
    else:
        try:
          support = SupportTicket.objects.get(id=supportid)
        except SupportTicket.DoesNotExist:
          support = ''
        try:
          supportdetail = SupportTicketDetails.objects.filter(ticket=supportid)
        except SupportTicketDetails.DoesNotExist:
          supportdetail = ''  
        form = SupportTicketDetailForm()
        context={
            'Title':'Support Detail',
            'form':form,
            'support':support,
            'supportdetail':supportdetail
           }
        
    return render(request,'support/supportdetailform.html', context)

def supportreply_view(request,supportid):
    context={}
    try:
        support = SupportTicket.objects.get(id=supportid)
    except SupportTicket.DoesNotExist:
        support = ''
    if request.method == 'POST':
       form = SupportTicketDetailAdminForm(request.POST, request.FILES)
       if form.is_valid():
          agree = form.cleaned_data['agree']
          updateagree = 0
          if agree == True:
            updateagree = 2
          elif agree == False:
            updateagree = 0
          form.instance.user_id = support.user.id
          form.instance.ticket_id = support.id
          form.instance.created_by_id  = request.user.id
          form.instance.created_on   = datetime.datetime.now()
          form.instance.modified_by = request.user
          form.save()
          updatesupport = SupportTicket.objects.get(id=supportid)
          updatesupport.status = updateagree
          updatesupport.save()
          messages.add_message(request, messages.SUCCESS, 'Reply message submitted successfully.')
          return HttpResponseRedirect('/support/detail_supportticket/'+str(supportid)+'/')
       else:
          messages.add_message(request, messages.ERROR, 'Old pattern is mismatch')
          return HttpResponseRedirect('/support/detail_supportticket/'+str(supportid)+'/')
       
       
    else:
        try:
          support = SupportTicket.objects.get(id=supportid)
        except SupportTicket.DoesNotExist:
          support = ''
        try:
          supportdetail = SupportTicketDetails.objects.filter(ticket=supportid)
        except SupportTicketDetails.DoesNotExist:
          supportdetail = ''  
        form = SupportTicketDetailAdminForm()
        
        context={
            'Title':'Support Detail',
            'form':form,
            'staticcontent_qs':support,
            'supportdetail':supportdetail,
            'activecls':'supportadmin',

           }
        
    return render(request,'support/ticketdetail_detail.html', context)

def get_common_cipher():
    return AES.new(settings.COMMON_ENCRYPTION_KEY.encode("utf8"),AES.MODE_CBC,settings.COMMON_16_BYTE_IV_FOR_AES.encode("utf8"))
def encrypt_with_common_cipher(cleartext):
    common_cipher = get_common_cipher()
    
    cleartext_length = len(cleartext)
    nearest_multiple_of_16 = 16 * math.ceil(cleartext_length/16)
    padded_cleartext = cleartext.rjust(nearest_multiple_of_16)
    raw_ciphertext = common_cipher.encrypt(padded_cleartext.encode("utf8"))
    return base64.b64encode(raw_ciphertext).decode('utf-8')
def decrypt_with_common_cipher(ciphertext):
    common_cipher = get_common_cipher()
    raw_ciphertext = base64.b64decode(ciphertext)
    decrypted_message_with_padding = common_cipher.decrypt(raw_ciphertext)
    return decrypted_message_with_padding.decode('utf-8').strip()
def get_common_cipher_setting():
    COMMON_ENCRYPTION_KEY='asdjk@15r32r1234asdsaeqwe314SEFT'
    COMMON_16_BYTE_IV_FOR_AES='IVIVIVIVIVIVIVIV'
    return AES.new(COMMON_ENCRYPTION_KEY,
                   AES.MODE_CBC,COMMON_16_BYTE_IV_FOR_AES
                   )
def decrypt_with_common_cipher_setting(ciphertext):
    common_cipher = get_common_cipher_setting()
    raw_ciphertext = base64.b64decode(ciphertext)
    decrypted_message_with_padding = common_cipher.decrypt(raw_ciphertext)
    return decrypted_message_with_padding.decode('utf-8').strip()


def get_email_template(request,email_temp_id):
    email_template = EmailTemplate.objects.get(id = email_temp_id)
    if email_template:
        email_template_qs =email_template
    else:
        email_template_qs = ''
    return email_template_qs


def newsletter_add(request):
    context={}
    marketpricelist = []
    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        companyfb= companyqs.fb
        companytwitter =companyqs.twitter
    except:
        companyqs = 'Global Experts '
        companyname = 'Global Experts '
        companyfb=''
        companytwitter=''
    try:
      user = NewsletterSubscribeUser.objects.filter(status=0)          
    except NewsletterSubscribeUser.DoesNotExist:
      user = None
          
    if user:
      for item in user:
        market_temp = {}
        market_temp['id'] = item.id
        market_temp['email'] = item.email
        marketpricelist.append(market_temp)

    
    if request.method == 'POST':
       
       category = request.POST.get('category', '')
       subject = request.POST.get('subject', '')
       message = request.POST.get('message', '')
       selected_values = request.POST.getlist('userlist')
       
       if selected_values != "":
          pass
          for i in selected_values:
            checkuser = NewsletterSubscribeUser.objects.get(id=i)
            checkemail =checkuser.email
            subjectemail = subject
            messageemail =message
            email_template = EmailTemplate.objects.get(id = 3)
            if email_template:
              email_template_qs =email_template
            else:
              email_template_qs = ''

            text_file = open("support/templates/support/newslettermail.html", "w")  
            text_file.write(email_template.content)
            text_file.close()
            email_subject = email_template.Subject
            to_email = checkemail
            from_email_get = settings.EMAIL_USER
            from_email =decrypt_with_common_cipher(from_email_get)
            hostuser= decrypt_with_common_cipher(settings.EMAIL_HOST_US)
            hostpwd=decrypt_with_common_cipher(settings.EMAIL_PASSWORD)
            currentYear = datetime.datetime.now().year
            settings.EMAIL_HOST_PASSWORD = hostpwd
            settings.EMAIL_HOST_USER = hostuser
            data= {
                'subject':subjectemail,
                'message': messageemail,
                'domain':settings.DOMAIN_URL,
                'protocol': 'http',
                'username':checkemail,
                'email':to_email,
                'company_logo':'comp_company_logo',
                'company_name':companyname,
                'years':currentYear,
                'fb':companyfb,
                'twitter':companytwitter
                }
            text_content = 'This is an important message.'
            htmly = get_template('support/newslettermail.html')
            html_content = htmly.render(data)
            msg = EmailMultiAlternatives(subjectemail, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
          
            messages.add_message(request, messages.SUCCESS, 'Submited Successfully')

       else:
          messages.add_message(request, messages.ERROR, 'The field must required')
          
          userlist = User.objects.filter(admin_user_profile__role=2)
          context={
              'Title':'Newsletter',
              'userlist':marketpricelist,
          }
      
    else:
          
      userlist = User.objects.filter(admin_user_profile__role=2)
      context={
            'Title':'Newsletter',
            'userlist':marketpricelist,
            'activecls':'newsletteradmin'
      }
        
    return render(request,'support/newsletter.html', context)

@ajax
def getuserlist_ajax(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    category = body['category']

    
    marketpricelist = []
    if category != '':
      if category == '0':
        try:
          user = User.objects.filter(admin_user_profile__role=2)
        except User.DoesNotExist:
          user = None
        
        if user:
            for item in user:
              market_temp = {}
              market_temp['id'] = item.id
              market_temp['email'] = item.email
              marketpricelist.append(market_temp)
        try:
          user = NewsletterSubscribeUser.objects.filter(status=0)
          
        except NewsletterSubscribeUser.DoesNotExist:
          user = None
          
        if user:
          for item in user:
            market_temp = {}
            market_temp['id'] = item.id
            market_temp['email'] = item.email
            marketpricelist.append(market_temp)

      elif category == '1':
        try:
          user = User.objects.filter(admin_user_profile__role=2)
        except User.DoesNotExist:
          user = None
        
        if user:
            for item in user:
              market_temp = {}
              market_temp['id'] = item.id
              market_temp['email'] = item.email
              marketpricelist.append(market_temp)

      elif category == '2':
        try:
          user = NewsletterSubscribeUser.objects.filter(status=0)
          
        except NewsletterSubscribeUser.DoesNotExist:
          user = None
          
        if user:
          for item in user:
            market_temp = {}
            market_temp['id'] = item.id
            market_temp['email'] = item.email
            marketpricelist.append(market_temp)

      elif category == '3':
        try:
          user = User.objects.filter(admin_user_profile__role=2)
        except User.DoesNotExist:
          user = None
        
        if user:
            for item in user:
              market_temp = {}
              market_temp['id'] = item.id
              market_temp['email'] = item.email
              marketpricelist.append(market_temp)
        try:
          user = NewsletterSubscribeUser.objects.filter(status=0)
          
        except NewsletterSubscribeUser.DoesNotExist:
          user = None
          
        if user:
          for item in user:
            market_temp = {}
            market_temp['id'] = item.id
            market_temp['email'] = item.email
            marketpricelist.append(market_temp)
      return JsonResponse({'status':'success','msg':'success','marketdatalist':marketpricelist})

    else:
      return JsonResponse({'status':'Error', 'msg': 'user assign unsuccessfully'})
    


