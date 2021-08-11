from django.shortcuts import render
from django.shortcuts import render,get_list_or_404, get_object_or_404
from django.conf import settings


from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView,FormView
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


import decimal
from decimal import *
from django.db.models import Q,F,Func,Value
from django.db.models import Count, Min,Max, Sum, Avg,DecimalField,DateTimeField,CharField
from django.db.models.expressions import RawSQL
from django.db.models.functions import Cast,TruncSecond,ExtractSecond


from django.db import transaction

from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model

from django.template import RequestContext

from trade_perms.mixins import OR_PermissionsRequiredMixin, shared_permission_access, admin_permission_access
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.core.exceptions import PermissionDenied
from auditable.views import AuditableMixin

from django.contrib.auth import update_session_auth_hash

from django.core import serializers


from django_ajax.decorators import ajax


from django_tables2 import RequestConfig


import requests
import json
import urllib

import pytz
import random
from random import randint

from django.template.loader import get_template
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from trade_admin_auth.mixins import get_client_ip,get_browser_type,get_browser_os_type,get_browser_device_type
from django.template import loader



from company.models import Company,Company_Settings
from trade_master.models import Cms_StaticContent
from trade_admin_auth.models import AdminUser_Profile,AdminUser_Activity
from trade_admin_auth.models import User_Kyc_Verification,User_Notification
from trade_master.models import Cms_StaticContent,Faq,EmailTemplate,Testimonial,Blog,Marketingvideo

from trade_auth.models import UserAddress
from trade_auth.forms import Contactform

from locations.models import Country


import uuid
import pyotp
from functools import wraps
import csv
from io import StringIO
from itertools import groupby
from dateutil.relativedelta import relativedelta
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import base64
import re
from Crypto.Cipher import AES

from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import base64, json, math

from django.views.generic.detail import DetailView

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from cryptotoken.models import TokenDetails,RoadMap,CurrencyDetails,TokenInformation
import os
dirpath = os.getcwd()
from django.http import FileResponse, Http404

def check_company(group_name):
    def _check_company(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                companyqs = Company.objects.get(id=1)
                companyname= companyqs.name
                companysite = companyqs.company_settings.site_maintenance_status
                comingsoon = companyqs.company_settings.new_coin_status
            except Company.DoesNotExist:
                companyqs = 'Global Experts'
                companyname = 'Global Experts'
                companysite = ''
                comingsoon=''
            if comingsoon == 1:
                return HttpResponseRedirect('/global/comingsoon/')
            return view_func(request, *args, **kwargs)
            if companysite == 1:
                return HttpResponseRedirect('/global/offline/')
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_company


class CompanyMaintanceRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        try:
            companyqs = Company.objects.get(id=1)
            companyname= companyqs.name
            companysite = companyqs.company_settings.site_maintenance_status
            
        except Company.DoesNotExist:
            companyqs = 'VotricUnited'
            companyname = 'VotricUnited'
            companysite = ''
        if companysite == 1:
            return HttpResponseRedirect('/finance/offline/')
        return super().dispatch(request, *args, **kwargs)



def check_walletaddress(group_name):
    def _check_walletaddress(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            userwalletaddress = ''
            
            if "walletaddress" in request.session.keys():
                walletaddress = request.session['walletaddress']
                try:
                    useraddress = UserAddress.objects.get(Q(useraddress = walletaddress))
                    userwalletaddress= useraddress.useraddress
                except UserAddress.DoesNotExist:
                    useraddress = ''
            print(userwalletaddress,'userwalletaddress')        
            if userwalletaddress == ''  or userwalletaddress == None:
                return HttpResponseRedirect('/')
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_walletaddress


def checkmessage(request,name):
    base64_message = name
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')

    return message


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

def offline_view(request):

    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        companysite = companyqs.company_settings_name.site_maintenance_status
    except:
        companyqs = 'Global Experts'
        companyname = 'Global Experts'
        companysite = ''
    context={
    'message':'site maintance'
    }

    return HttpResponse(loader.render_to_string('trade_auth/under_construction.html', context), status=503)    

def comingsoon_view(request):
    try:
        companyqs = Company.objects.get(id=1)
        companyid=companyqs.id
        companyname= companyqs.name
    except Company.DoesNotExist:
        companyqs = 'Global Experts'
        companyname = 'Global Experts'
        companyid=''
    try:
        companysetting = Company_Settings.objects.get(company_settings_name = companyid)
        comingsoonmsg=companysetting.site_maintenance
        companysite = companysetting.new_coin_status
    except Company_Settings.DoesNotExist:
        companysetting=''
        comingsoonmsg=''
        companysite = ''
    try:
        currencydetails =CurrencyDetails.objects.get(id=1)
    except:
        currencydetails = ''
    context={
    'companyqs':companyqs,
    'currencydetails':currencydetails,
    'message':'Coming Soon',
    'companysite':companysite,
    'comingsoonmsg':comingsoonmsg
    }
        
    return render(request,"trade_auth/comingsoon.html",context)
@check_company('site')
def home(request):
    context={}
    context['Title'] = 'Home'
    try:
        faq_qs = Faq.objects.filter(status=0)
    except Faq.DoesNotExist:
        faq_qs = ''
    
    try:
        roadmap = RoadMap.objects.filter(status=0).order_by('id')
    except RoadMap.DoesNotExist:
        roadmap = ''
    try:
        currencydetails =CurrencyDetails.objects.get(id=1)
    except:
        currencydetails = ''
    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        company_fb = companyqs.fb
        company_linkedin = companyqs.linkedin
        company_telegram = companyqs.gplus
        company_twitter = companyqs.twitter
        company_instagram = companyqs.instagram

    
    except:
        companyqs = 'Global Experts '
        companyname = 'Global Experts '
        company_fb = ""
        company_linkedin = ""   
        company_telegram=""
        company_twitter=""
        company_instagram=""

    try:
        video=Company_Settings.objects.get(id=1)
        marketingvideo_one = video.depositurl
        marketingvideo_two = video.withdrawurl
        marketingvideo_three = video.coinmarket
    except:
        marketingvideo_one = ''
        marketingvideo_two = ''
        marketingvideo_three = ''

    try:
        content_discover= Cms_StaticContent.objects.get(Q(name='bannersubtitle') & Q(contenttype=1))
        content_bannerone= Cms_StaticContent.objects.get(Q(name='bannercontentone') & Q(contenttype=1))
        content_subtitle= Cms_StaticContent.objects.get(Q(name='bannercontenttwo') & Q(contenttype=1))
        content_burnedvalue= Cms_StaticContent.objects.get(Q(name='valueamt') & Q(contenttype=1))
        content_valueamount= Cms_StaticContent.objects.get(Q(name='burnedamount') & Q(contenttype=1))
        content_aboutus= Cms_StaticContent.objects.get(Q(name='aboutustitle') & Q(contenttype=1))
        content_aboutuscontent= Cms_StaticContent.objects.get(Q(name='aboutuscontent') & Q(contenttype=1))
        aboutussubone= Cms_StaticContent.objects.get(Q(name='aboutussubone') & Q(contenttype=1))
        aboutussubtwo= Cms_StaticContent.objects.get(Q(name='aboutussubtwo') & Q(contenttype=1))
        aboutussubthree= Cms_StaticContent.objects.get(Q(name='aboutussubthree') & Q(contenttype=1))
        aboutussubfour= Cms_StaticContent.objects.get(Q(name='aboutussubfour') & Q(contenttype=1))
        tokenheading= Cms_StaticContent.objects.get(Q(name='tokenheading') & Q(contenttype=1))
        tokenvalue= Cms_StaticContent.objects.get(Q(name='tokenvalue') & Q(contenttype=1))
        tokenholder= Cms_StaticContent.objects.get(Q(name='tokenholder') & Q(contenttype=1))
        tokenliquidity= Cms_StaticContent.objects.get(Q(name='tokenliquidity') & Q(contenttype=1))
        tokenmarket= Cms_StaticContent.objects.get(Q(name='tokenmarket') & Q(contenttype=1))
        tokenburned= Cms_StaticContent.objects.get(Q(name='tokenburned') & Q(contenttype=1))
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
        dxbfeature= Cms_StaticContent.objects.get(Q(name='dxbfeature') & Q(contenttype=1))
        dxbcontentone =  Cms_StaticContent.objects.get(Q(name='dxbcontentone') & Q(contenttype=1))
        dxbcontentwo = Cms_StaticContent.objects.get(Q(name='dxbcontenttwo') & Q(contenttype=1))
        dxbcontentthree = Cms_StaticContent.objects.get(Q(name='dxbcontenthree') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        content_discover = ''
        content_bannerone = ''
        content_subtitle = ''
        content_burnedvalue =''
        content_valueamount =''
        content_aboutus =''
        content_aboutuscontent =''
        aboutussubone=''
        aboutussubtwo =''
        aboutussubthree=''
        aboutussubfour =''
        tokenheading=''
        tokenvalue=''
        tokenholder=''
        tokenliquidity=''
        tokenmarket=''
        tokenburned=''
        howitstart=''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
        dxbfeature=''
        dxbcontentone=''
        dxbcontentwo=''
        dxbcontentthree=''

    try:
        blogqs =Marketingvideo.objects.filter(status=0).order_by('id')[:3]
    except: 
        blogqs = ""

    context['faq_qs'] = faq_qs 
    context['roadmap'] = roadmap
    context['currencydetails']=currencydetails
    context['content_discover'] =content_discover
    context['content_bannerone'] =content_bannerone
    context['content_subtitle'] =content_subtitle
    context['content_burnedvalue'] =content_burnedvalue
    context['content_valueamount'] =content_valueamount
    context['content_aboutus'] =content_aboutus
    context['content_aboutuscontent'] =content_aboutuscontent
    context['aboutussubone'] =aboutussubone
    context['aboutussubtwo'] =aboutussubtwo
    context['aboutussubthree'] =aboutussubthree
    context['aboutussubfour'] =aboutussubfour
    context['tokenheading'] =tokenheading
    context['tokenvalue'] =tokenvalue
    context['tokenholder']=tokenholder
    context['tokenliquidity'] =tokenliquidity
    context['tokenmarket'] =tokenmarket
    context['tokenburned'] =tokenburned
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['companyqs']=companyqs
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    context['activetab']='home'
    context['dxbfeature']=dxbfeature
    context['dxbcontentone']=dxbcontentone
    context['dxbcontentwo']=dxbcontentwo
    context['dxbcontentthree']=dxbcontentthree
    
    context['company_fb']=company_fb
    context['company_linkedin']=company_linkedin
    context['company_telegram']=company_telegram
    context['company_twitter']=company_twitter
    context['company_instagram']=company_instagram

    context['marketingvideo_one']=marketingvideo_one
    context['marketingvideo_two']=marketingvideo_two
    context['marketingvideo_three']=marketingvideo_three
    context['blogqs']=blogqs

    return render(request,"trade_auth/home.html",context)

@check_company('site')
def contactus(request):
    context={}
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
    context['Title'] ='Contactus'
    context['companyqs'] = companyqs
    context['keywords'] = 'Global Experts'
    context['content']='contactus ask questions there for a free and open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='contactus'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    if  request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
        'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
        'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if result['success']:
            form = Contactform(request.POST)
            if form.is_valid():
                form.instance.created_on   = datetime.datetime.now()
                form.instance.status   = 0
                contactform = form.save()

                emailtemplate = get_email_template(request,1)
                text_file = open("trade_auth/templates/emailtemplate/contactus_mail.html", "w")
                text_file.write(emailtemplate.content)
                text_file.close()
                
               
                email_subject = emailtemplate.Subject
                to_email = contactform.email
                from_email_get = settings.EMAIL_USER
                from_email =decrypt_with_common_cipher(from_email_get)
                hostuser= decrypt_with_common_cipher(settings.EMAIL_HOST_US)
                hostpwd=decrypt_with_common_cipher(settings.EMAIL_PASSWORD)
                settings.EMAIL_HOST_PASSWORD = hostpwd
                settings.EMAIL_HOST_USER = hostuser
                currentYear = datetime.datetime.now().year
                
                data= {
                    'username':contactform.name,
                    'email':contactform.email,
                    'msg': contactform.message,
                    'company_name':companyname,
                    'years':currentYear,
                    'fb':companyfb,
                    'twitter':companytwitter
                    }
                text_content = 'This is an important message.'
                htmly = get_template('emailtemplate/contactus_mail.html')
                html_content = htmly.render(data)
                msg = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
                msg.attach_alternative(html_content, "text/html")
                msg.send()

                messages.add_message(request, messages.SUCCESS, 'Your Enquiry successfully posted. Admin will be contact soon.')
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid values are entered.')
                return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.WARNING,'Please validate Captcha')
            return HttpResponseRedirect('/global/contactus/')

    else:
        return render(request,"trade_auth/contact.html",context)



@check_company('site')
def aboutus(request):
    context={}
    context['Title'] ='About Us'
    context['keywords'] = 'About Us'
    context['content']='Global Experts About Us open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='aboutus'
    try:
        currencydetails =CurrencyDetails.objects.get(id=1)
    except:
        currencydetails = ''
    context['currencydetails'] = currencydetails
    try:
        tokenvalue= Cms_StaticContent.objects.get(Q(name='tokenvalue') & Q(contenttype=1))
        tokenholder= Cms_StaticContent.objects.get(Q(name='tokenholder') & Q(contenttype=1))
        tokenliquidity= Cms_StaticContent.objects.get(Q(name='tokenliquidity') & Q(contenttype=1))
        aboutuspage= Cms_StaticContent.objects.get(Q(name='aboutuspage') & Q(contenttype=0))
        aboutuscontent1= Cms_StaticContent.objects.get(Q(name='aboutuscontent1') & Q(contenttype=0))
        aboutuscontent2= Cms_StaticContent.objects.get(Q(name='aboutuscontent2') & Q(contenttype=0))
        aboutuscontent3= Cms_StaticContent.objects.get(Q(name='aboutuscontent3') & Q(contenttype=0))
    except Cms_StaticContent.DoesNotExist:
        tokenvalue =''
        tokenholder=''
        aboutuspage=''
        tokenliquidity =''
        aboutuscontent1=''
        aboutuscontent2=''
        aboutuscontent3=''
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    context['tokenvalue'] =tokenvalue
    context['tokenholder']=tokenholder
    context['tokenliquidity'] =tokenliquidity
    context['aboutuspage'] =aboutuspage
    context['aboutuscontent1'] =aboutuscontent1
    context['aboutuscontent2']=aboutuscontent2
    context['aboutuscontent3'] =aboutuscontent3
    return render(request,"trade_auth/aboutus.html",context)

@check_company('site')
def whitepaper(request):
    context={}
    context['Title'] ='WhitePaper'
    context['keywords'] = 'WhitePaper'
    context['content']='Global Experts WhitePaper open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='whitepaper'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    try:
        currencydetails =CurrencyDetails.objects.get(id=1)
    except:
        currencydetails = ''
    context['currencydetails'] = currencydetails
    return render(request,"trade_auth/whitepaper.html",context)

@check_company('site')
def buytoken(request):
    context={}
    context['Title'] ='Buy Token'
    context['keywords'] = 'Buy Token'
    context['content']='Global Experts Buy Token open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='buytoken'
    try:
        aboutussubone= Cms_StaticContent.objects.get(Q(name='aboutussubone') & Q(contenttype=1))
        aboutussubtwo= Cms_StaticContent.objects.get(Q(name='aboutussubtwo') & Q(contenttype=1))
        aboutussubthree= Cms_StaticContent.objects.get(Q(name='aboutussubthree') & Q(contenttype=1))
        aboutussubfour= Cms_StaticContent.objects.get(Q(name='aboutussubfour') & Q(contenttype=1))
        tokenheading= Cms_StaticContent.objects.get(Q(name='tokenheading') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        aboutussubone=''
        aboutussubtwo =''
        aboutussubthree=''
        aboutussubfour =''
        tokenheading=''
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    context['aboutussubone'] =aboutussubone
    context['aboutussubtwo'] =aboutussubtwo
    context['aboutussubthree'] =aboutussubthree
    context['aboutussubfour'] =aboutussubfour
    context['tokenheading'] =tokenheading
    return render(request,"trade_auth/buytoken.html",context)

@check_company('site')
def ourteam(request):
    context={}
    context['Title'] ='Our Team'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts Our Team open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='ourteam'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    try:
        testimonialqs = Testimonial.objects.filter(Q(status=0)).order_by('id')
    except Testimonial.DoesNotExist:
        testimonialqs = ''
    context['testimonialqs']=testimonialqs
    return render(request,"trade_auth/ourteam.html",context)


@check_company('site')
def roadmap(request):
    context={}
    context['Title'] ='RoadMap'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts RoadMap open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='roadmap'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    try:
        roadmap = RoadMap.objects.filter(status=0).order_by('id')
    except RoadMap.DoesNotExist:
        roadmap = ''
    context['roadmap']=roadmap
    return render(request,"trade_auth/roadmap.html",context)


@check_company('site')
def faq(request):
    context={}
    context['Title'] ='FAQ'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts FAQ free and open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='faq'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    faq_qs = Faq.objects.filter(status=0)
    faq_res =''
    if faq_qs:
        faq_res =faq_qs
    else:
        faq_res =''
    if request.method == 'POST':
        
        get_searchname = request.POST.get('search','')
        faq_res = Faq.objects.filter(Q(status =0) & Q(title__icontains=get_searchname) | Q(content__icontains=get_searchname)).order_by('id')
    else:
        faq_res = faq_qs
    context['faq_qs']=  faq_res
      
    return render(request,"trade_auth/faq.html",context)
@check_company('site')
def privacy(request):
    context={}
    context['Title'] ='Privacy Policy'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts Privacy Policy free and open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='privacy'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    cms_content = Cms_StaticContent.objects.get(name='privacypolicy')
    if cms_content:
        cms_content_res = cms_content
    else:
        cms_content_res =''
    cms_contenttwo = Cms_StaticContent.objects.get(name='privacypolicytwo')
    if cms_contenttwo:
        cms_content_twores = cms_contenttwo
    else:
        cms_content_twores =''
    context['cms_content'] = cms_content_res
    context['cms_content_twores'] = cms_content_twores
    return render(request,"trade_auth/privacy.html",context)

@check_company('site')
def terms(request):
    context={}
    context['Title'] ='Terms of Use'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts Terms of Use free and open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='terms'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    cms_content = Cms_StaticContent.objects.get(name='terms')
    if cms_content:
        cms_content_res = cms_content
    else:
        cms_content_res =''
    cms_contenttwo = Cms_StaticContent.objects.get(name='termstwo')
    if cms_contenttwo:
        cms_content_twores = cms_contenttwo
    else:
        cms_content_twores =''
    context['cms_content'] = cms_content_res
    context['cms_content_twores'] = cms_content_twores
    return render(request,"trade_auth/terms.html",context)


@check_company('site')
@check_walletaddress('address')
def walletdetails(request):
    context={}
    context['Title'] ='Wallet Details'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts Wallet Details free and open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='walletdetails'
    context['currentpage']='walletdetails'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter  
    try:
        currencydetails= CurrencyDetails.objects.get(id=1)
        get_currency_dt1=currencydetails.timerdate
        get_currency_dt =currencydetails.timerdate.replace(tzinfo=None)
        updated_time = (get_currency_dt + timedelta(hours=2))
        updated_date = (get_currency_dt + relativedelta(months=+6))
        current_time = datetime.datetime.today()
        current_time1 = current_time.replace(microsecond=0)
        claimbotton_enable = ''
        print(current_time1,'current_time1')
        print(get_currency_dt,'get_currency_dt')
        if current_time1 > get_currency_dt:
            claimbotton_enable = 'Yes'
        else:
            claimbotton_enable = 'No'
        
    except CurrencyDetails.DoesNotExist:
        currencydetails = ''
        get_currency_dt=''
        updated_time = ''
        claimbotton_enable =''
    print(claimbotton_enable,'claimbotton_enable')    
    context['currencydetails'] = currencydetails
    context['currency_date'] = get_currency_dt
    context['updated_date'] = updated_date
    context['updated_time'] = updated_time
    context['claimbotton_enable'] = claimbotton_enable
    return render(request,"trade_auth/walletdetails.html",context)


@check_company('site')
def disconnectwallet(request):
    context={}
    context['Title'] ='Disconnect Wallet'
    context['keywords'] = 'Global Experts'
    context['content']='Global Experts Terms of Use free and open discussion about cryptocurrency with others in the Global Experts community.'
    context['activetab']='disconnect'
    if "walletaddress" in request.session.keys():
        del request.session['walletaddress']
        messages.add_message(request, messages.SUCCESS, 'Wallet Disconnect successfully.')
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    

@ajax
def connection_wallet(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    burneraddress = body['address']
    if burneraddress != '' and burneraddress != None:
        try:
            checkuseraddress = UserAddress.objects.get(useraddress =burneraddress)
            useraddress = checkuseraddress.useraddress
            request.session['walletaddress'] = burneraddress
            return JsonResponse({'status':'successlogin', 'msg': 'address matched successfully'})
        except:
            updateuseraddress = UserAddress.objects.create(
                useraddress=burneraddress,
                contractid=1,
                status=0,
                created_on=datetime.datetime.now(),
            )
            useraddress = updateuseraddress.id
            checkuseraddress = ''
            request.session['walletaddress'] = burneraddress
            return JsonResponse({'status':'successregistered', 'msg': 'address registered successfully'})
        
    else:
      return JsonResponse({'status':'Error', 'msg': 'Metamask not connected.'})



@check_company('site')
def blog_list(request):
    context={}
    context['Title'] ='Blog list'
    context['keywords'] = 'Blog'
    context['activetab']='blog'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''

    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        company_fb = companyqs.fb
        company_linkedin = companyqs.linkedin
        company_telegram = companyqs.gplus
        company_twitter = companyqs.twitter
        print(company_twitter,'company_twitter')
        company_instagram = companyqs.instagram
        print(company_instagram,'company_instagram')
    except:
        companyqs = 'Global Experts '
        companyname = 'Global Experts '
        company_fb = ""
        company_linkedin = ""   
        company_telegram=""
        company_twitter=""
        company_instagram=""
   
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    try:
        blogqs =Blog.objects.filter(status=0).order_by('id')
    except:
        blogqs = ''
    context['blogqs'] = blogqs
    context['company_fb']=company_fb
    context['company_linkedin']=company_linkedin
    context['company_telegram']=company_telegram
    context['company_twitter']=company_twitter
    context['company_instagram']=company_instagram
    return render(request,"trade_auth/blog.html",context)




@check_company('site')
def blog_list(request):
    context={}
    context['Title'] ='Blog list'
    context['keywords'] = 'Blog'
    context['activetab']='blog'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''

    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        company_fb = companyqs.fb
        company_linkedin = companyqs.linkedin
        company_telegram = companyqs.gplus
        company_twitter = companyqs.twitter
        print(company_twitter,'company_twitter')
        company_instagram = companyqs.instagram
        print(company_instagram,'company_instagram')
    except:
        companyqs = 'Global Experts '
        companyname = 'Global Experts '
        company_fb = ""
        company_linkedin = ""   
        company_telegram=""
        company_twitter=""
        company_instagram=""
   
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    try:
        blogqs =Blog.objects.filter(status=0).order_by('id')
    except:
        blogqs = ''
    context['blogqs'] = blogqs
    context['company_fb']=company_fb
    context['company_linkedin']=company_linkedin
    context['company_telegram']=company_telegram
    context['company_twitter']=company_twitter
    context['company_instagram']=company_instagram
    return render(request,"trade_auth/blog.html",context)




@check_company('site')
def info_blog(request,id):
    print("7530068643")
    context={}
    context['Title'] ='Blog list'
    context['keywords'] = 'Blog'
    context['activetab']='blog'
    try:
        blog =Blog.objects.get(id=id)
        print(blog,'blog')
    except:
        blog = ''
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''

    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        company_fb = companyqs.fb
        company_linkedin = companyqs.linkedin
        company_telegram = companyqs.gplus
        company_twitter = companyqs.twitter
        print(company_twitter,'company_twitter')
        company_instagram = companyqs.instagram
        print(company_instagram,'company_instagram')
    except:
        companyqs = 'Global Experts '
        companyname = 'Global Experts '
        company_fb = ""
        company_linkedin = ""   
        company_telegram=""
        company_twitter=""
        company_instagram=""
   
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter

    context['blog'] = blog
    context['company_fb']=company_fb
    context['company_linkedin']=company_linkedin
    context['company_telegram']=company_telegram
    context['company_twitter']=company_twitter
    context['company_instagram']=company_instagram
    return render(request,"trade_auth/blog_detail.html",context)



@check_company('site')
def video_list(request):
    context={}
    context['Title'] ='Blog list'
    context['keywords'] = 'Blog'
    context['activetab']='blog'
    try:
        howitstart= Cms_StaticContent.objects.get(Q(name='howitstart') & Q(contenttype=1))
        howtobbf= Cms_StaticContent.objects.get(Q(name='howtobbf') & Q(contenttype=1))
        aboutfooter= Cms_StaticContent.objects.get(Q(name='aboutfooter') & Q(contenttype=1))
        helpfooter= Cms_StaticContent.objects.get(Q(name='helpfooter') & Q(contenttype=1))
    except Cms_StaticContent.DoesNotExist:
        howitstart = ''
        howtobbf=''
        aboutfooter=''
        helpfooter=''

    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        company_fb = companyqs.fb
        company_linkedin = companyqs.linkedin
        company_telegram = companyqs.gplus
        company_twitter = companyqs.twitter
        company_instagram = companyqs.instagram
    except:
        companyqs = 'Global Experts '
        companyname = 'Global Experts '
        company_fb = ""
        company_linkedin = ""   
        company_telegram=""
        company_twitter=""
        company_instagram=""
   
    context['howitstart'] =howitstart
    context['howtobbf'] =howtobbf
    context['aboutfooter']=aboutfooter
    context['helpfooter']=helpfooter
    try:
        blogqs =Marketingvideo.objects.filter(status=0).order_by('id')
    except:
        blogqs = ''
    context['blogqs'] = blogqs
    context['company_fb']=company_fb
    context['company_linkedin']=company_linkedin
    context['company_telegram']=company_telegram
    context['company_twitter']=company_twitter
    context['company_instagram']=company_instagram
    return render(request,"trade_auth/marketing_video.html",context)

