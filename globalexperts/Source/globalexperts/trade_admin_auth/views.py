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
import string
import random

from django.db.models import Q,F,Func,Value
from django.db.models import Count, Min,Max, Sum, Avg,DecimalField,DateTimeField,CharField
from django.db.models.expressions import RawSQL
from django.db.models.functions import Cast,TruncSecond,ExtractSecond


from django.db import transaction

from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView

from trade_perms.mixins import OR_PermissionsRequiredMixin, shared_permission_access, admin_permission_access
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.core.exceptions import PermissionDenied
from auditable.views import AuditableMixin


from django_ajax.decorators import ajax
from django.core.mail import send_mail

from django_tables2 import RequestConfig
from django_tables2 import RequestConfig
from crispy_forms.layout import Submit,ButtonHolder,Reset


from trade_admin_auth.mixins import check_group
from trade_admin_auth.mixins import SubAdminRequiredMixin,CheckIpaddressAdminRequiredMixin
from trade_admin_auth.mixins import get_client_ip,get_browser_type,get_browser_os_type,get_browser_device_type,allow_by_ip,check_adminip
from trade_admin_auth.mixins import ManageUserAdminRequiredMixin,ManageBlockipAdminRequiredMixin
from operator import itemgetter


from company.models import Company,Company_Settings
from modules.models import MenuModules
from trade_admin_auth.models import AdminUser_Profile,MenuPermissions,AdminUser_Activity,User_Kyc_Verification
from trade_master.models import Contactus
from support.models import NewsletterSubscribeUser

from django.contrib.auth.forms import PasswordChangeForm

from trade_auth.models import UserAddress
from trade_auth.views import get_email_template,checkmessage,encrypt_with_common_cipher,decrypt_with_common_cipher

from trade_admin_auth.forms import EditCompanyForm,EditCompanySettingsForm,EditCompanyMultiForm
from trade_admin_auth.forms import AdminMenuPermissionForm,AdminUserAddForm,AdminUserAddMultiForm
from trade_admin_auth.forms import AdminUserEditMultiForm,KycupdateForm,ChangePatternForm,AdminUserEditSubadminMultiForm
from trade_admin_auth.forms import GoogleTokenVerificationForm
from trade_admin_auth.tables import UserAddressTable
import uuid
import pyotp

from django.utils import timezone

def Page403View(request):
	return render(request,'trade_admin_auth/403page.html',status=403)

def Page404View(request):
	return render(request,'trade_admin_auth/404page.html',status=404)

def Page500View(request):
	return render(request,'trade_admin_auth/500page.html',status=500)

def IPBlock404View(request):
  return render(request,'trade_admin_auth/ipblock404.html',status=404)

@check_adminip('checkadminip')
def adminlogin(request):
	context ={}
	context.update(csrf(request))
	return render(request, 'trade_admin_auth/login.html', context)

def adminlogin_auth(request):
    get_username = request.POST.get('username', '')
    get_password = request.POST.get('password', '')
    get_patterncode = request.POST.get('pattern_code', '')
    encrypt_username=encrypt_with_common_cipher(get_username)
    decrypt_username=decrypt_with_common_cipher(encrypt_username)
    try:
        if '@' in get_username:
          try:
            userprofile= AdminUser_Profile.objects.get(emailaddress =encrypt_username)
            if userprofile:
              useremail = userprofile.user.username
              username = User.objects.get(username=useremail).username
            else:
              username =''
          except AdminUser_Profile.DoesNotExist:
            userprofile =''
            username =''
        else:
            username = ''
        user = auth.authenticate(request=request,username=username,
                                 password=get_password)
    except User.DoesNotExist:
        user = None
    if user is not None:
        user_id = user.id
        get_userprofile = AdminUser_Profile.objects.get(user_id=user_id)
        user_pattern = get_userprofile.pattern_code
    else:
        user_pattern = ''
        
    if user is not None:
        if user_pattern is not None and user_pattern == int(get_patterncode):
            if user is not None and user.is_active:
                if user.groups.filter(name='Adminusers').exists():
                    userid = user.id
                    userprofile = AdminUser_Profile.objects.get(user = userid)
                    userprofile2fa = userprofile.twofa
                    if userprofile2fa == False:
                      auth.login(request, user)
                      print ('authenticated')
                      next_URL = '/tradeadmin/dashboard/'
                      admin_activity_history(request, user.id,
                            typelogin='Login')
                      return HttpResponseRedirect(next_URL)
                    elif userprofile2fa == True:
                      next_URL= '/tradeadmin/twofaadmin/'+str(userid)+'/'
                      return HttpResponseRedirect(next_URL)
                else:
                    messages.add_message(request, messages.ERROR, 'Login Details are invalid')
                    return HttpResponseRedirect('/LELPMDfDsmez0ksi/')
            else:
                messages.add_message(request, messages.ERROR, 'Login Details are invalid')
                return HttpResponseRedirect('/LELPMDfDsmez0ksi/')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid pattern code')
            return HttpResponseRedirect('/LELPMDfDsmez0ksi/')
    else:
        messages.add_message(request, messages.ERROR, 'Login Details are invalid')
        return HttpResponseRedirect('/LELPMDfDsmez0ksi/')

def admintwofa(request,uid):
    context={}
    context = {
    'Title':'Two Factor Authenticator',
    'keywords':'Enable Google Authenticator,QR Code',
    'content':'Enable Google Authenticator  for additional security for user.',
    }
    if request.method == 'POST':
        form = GoogleTokenVerificationForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.get(pk=uid)
                user_id = user.id
                get_userprofile = AdminUser_Profile.objects.get(user = user_id)
            except User.DoesNotExist:
                user = None
                get_userprofile = None
            if user is not None and get_userprofile is not None:
                secertkey = get_userprofile.google_id
                authtoken = pyotp.TOTP(secertkey)
                verification = authtoken.now()
                token = request.POST['token']
                if token == verification:
                    auth.login(request,user,backend='django.contrib.auth.backends.ModelBackend')
                    admin_activity_history(request,user_id,typelogin='Login')
                    messages.add_message(request, messages.SUCCESS, 'two factor authentication login successfully.')
                    return HttpResponseRedirect('/tradeadmin/dashboard/')
                else:
                    messages.add_message(request, messages.ERROR,'Invalid 2FA Code')
                    return HttpResponseRedirect('/tradeadmin/twofaadmin/'+str(user_id)+'/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid user!')
                return HttpResponseRedirect('/tradeadmin/twofaadmin/'+str(user_id)+'/')
    else:
        form = GoogleTokenVerificationForm()
    return render(request, 'trade_admin_auth/twofalogin.html', {'form': form})



def log_out(request):
    admin_activity_history(request,request.user.id,typelogin='Logout')
    auth.logout(request)
    return HttpResponseRedirect('/LELPMDfDsmez0ksi/')



def admin_activity_history(request,user_id,typelogin):
    get_user = User.objects.get(id=user_id)
    if get_user:
          create_admin_login = AdminUser_Activity.objects.create(
            user_id=user_id,
            ip_address=get_client_ip(request),
            activity=typelogin,
            browsername=get_browser_type(request),
            os=get_browser_os_type(request),
            devices=get_browser_device_type(request),
            created_on=datetime.datetime.now(),
            created_by_id = get_user.id,
            modified_by_id = get_user.id

          )   

    return  True
@check_adminip('checkadminip')
def dashboard(request):
    context={}
    get_user = Contactus.objects.filter(status=0)
    today = date.today()
    get_count_newsletter = NewsletterSubscribeUser.objects.filter(created_on__startswith=today)
    context['newsletter'] = len(get_count_newsletter)
    context['tradeuser'] = len(get_user)
    context['Title'] = 'Dashboard'
    context['dashboardshow'] = 'Yes'
    return render(request,"trade_admin_auth/dashboard.html",context)


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def adminforgotpassword(request):
  context ={}
  if  request.method == 'POST':
    get_email = request.POST.get('email','')
    encrypt_username=encrypt_with_common_cipher(get_email)
    try:
      userprofile= AdminUser_Profile.objects.get(emailaddress =encrypt_username)
      if userprofile:
        useremail = userprofile.user.username
        get_user = User.objects.get(Q(username = useremail) & Q(is_superuser=True))
        
      if get_user.groups.filter(name='Adminusers').exists():
        get_checkemail = userprofile.emailaddress
        checkemail = decrypt_with_common_cipher(get_checkemail)
        checkuser_id = get_user.id
    except AdminUser_Profile.DoesNotExist:
      get_user = None
      checkemail = None
      checkuser_id = None
    if checkemail is not None:
      generate_password = randomString(8)
      get_user.set_password(generate_password)
      get_user.save()
      
      subject ='Global Experts Forgot Password .'
      message ='Your admin password is '+generate_password
      from_email_get = settings.EMAIL_USER
      from_email =decrypt_with_common_cipher(from_email_get)
      hostuser= decrypt_with_common_cipher(settings.EMAIL_HOST_US)
      hostpwd=decrypt_with_common_cipher(settings.EMAIL_PASSWORD)
      settings.EMAIL_HOST_PASSWORD = hostpwd
      settings.EMAIL_HOST_USER = hostuser
      to_email = checkemail
      send_mail(subject, message, from_email, [to_email,])
      messages.add_message(request, messages.SUCCESS, 'Your Password sent to  your Email Address.') 
      return HttpResponseRedirect('/LELPMDfDsmez0ksi/')
    else:
      messages.add_message(request, messages.ERROR, 'Invalid Email Address')  
      return HttpResponseRedirect(reverse('trade_admin_auth:adminforgotpassword'))
  else:
    return render(request,"trade_admin_auth/adminforgot.html",context)    


class EditCompanySetting(CheckIpaddressAdminRequiredMixin,UpdateView):
    permission_required = ('trade_perms.Trade_Admin')
    raise_exception  = True
    model=Company
    form_class = EditCompanyMultiForm
    template_name = 'trade_admin_auth/settings.html'
    def get_context_data(self, **kwargs):
       context = super(EditCompanySetting, self).get_context_data(**kwargs)
       
       context['Title']='General Settings'
       return context
    def get_form_kwargs(self):
        kwargs = super(EditCompanySetting, self).get_form_kwargs()
        kwargs.update(instance={
            'form1': self.object,
            'form2': self.object.company_settings,
        })
        return kwargs
    def get_success_url(self, **kwargs):
        p_key = int(self.kwargs['pk'])
        messages.add_message(self.request, messages.SUCCESS, 'Setting Updated Successfully.')
        return '{}'.format(reverse('trade_admin_auth:general_settings', kwargs={'pk': p_key}))




class EditProfileSetting(CheckIpaddressAdminRequiredMixin,UpdateView):    
    model=User
    form_class = AdminUserEditMultiForm
    template_name = 'trade_admin_auth/profile.html'
    def get_context_data(self, **kwargs):
       context = super(EditProfileSetting, self).get_context_data(**kwargs)
       
       context['Title']='Profile Settings'
       return context
    def get_form_kwargs(self):
        kwargs = super(EditProfileSetting, self).get_form_kwargs()
        kwargs.update(instance={
            'form1': self.object,
            'form2': self.object.admin_user_profile,
        })
        return kwargs
    def get_success_url(self, **kwargs):
        p_key = int(self.kwargs['pk'])
        messages.add_message(self.request, messages.SUCCESS, 'Profile details updated Successfully.')
        return '{}'.format(reverse('trade_admin_auth:profile_settings', kwargs={'pk': p_key}))


class ChangePasswordView(PasswordChangeView):
  
    template_name = 'trade_admin_auth/changepassword.html'
    form_class = PasswordChangeForm
   
    def get_context_data(self, **kwargs):
       context = super(ChangePasswordView, self).get_context_data(**kwargs)
       context['Title']='Change Password'
       return context
   
    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Change password updated Successfully.')
        return '{}'.format(reverse('trade_admin_auth:change_password'))

class ChangePatternView(UpdateView):
    model= AdminUser_Profile
    template_name = 'trade_admin_auth/changepattern.html'
    form_class = ChangePatternForm
   
    def get_context_data(self, **kwargs):
       context = super(ChangePatternView, self).get_context_data(**kwargs)
       context['Title']='Change Pattern'
       return context
    @transaction.atomic
    def form_valid(self, form):
        formsave=form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Change pattern updated Successfully.')
        return HttpResponseRedirect(reverse('trade_admin_auth:patternchange',kwargs={'pk': formsave.id}))
    
def change_pattern_view(request,user_id):
    context={}
    user= User.objects.get(id=user_id)
    user_profile_id = user.admin_user_profile.id
    user_profile_pattern = user.admin_user_profile.pattern_code
    
    if request.method == 'POST':
       get_pattern_code = request.POST['pattern_code']
       get_oldpattern = request.POST['old_pattern_code']
       get_confirmpattern = request.POST['confirmpattern_code']
       
       pattern_code = int(get_pattern_code)
       oldpattern = int(get_oldpattern)
       confirmpattern = int(get_confirmpattern)
       if oldpattern !="" and confirmpattern != "" and pattern_code != "":
        if pattern_code == confirmpattern:
         if oldpattern != "" and oldpattern == user_profile_pattern:
           if pattern_code != "":
              update_patterncode = AdminUser_Profile.objects.get(id = user_profile_id)
              update_patterncode.pattern_code = pattern_code
              update_patterncode.save()
              messages.add_message(request, messages.SUCCESS, 'Change pattern updated Successfully.')
           else:
              messages.add_message(request, messages.ERROR, 'New pattern must required.')
              return HttpResponseRedirect('/tradeadmin/patternchange/'+str(user_id)+'/')
         else:
            messages.add_message(request, messages.ERROR, 'Old pattern is mismatch')
            return HttpResponseRedirect('/tradeadmin/patternchange/'+str(user_id)+'/')
        else:
            messages.add_message(request, messages.ERROR, 'Confirm pattern is mismatch')
            return HttpResponseRedirect('/tradeadmin/patternchange/'+str(user_id)+'/')
       else:
          messages.add_message(request, messages.ERROR, 'Pattern Code must required')
          return HttpResponseRedirect('/tradeadmin/patternchange/'+str(user_id)+'/')
       return HttpResponseRedirect('/tradeadmin/patternchange/'+str(user_id)+'/')
    else:
          
        
        context={
            'Title':'Change Pattern',
            'patterncode':user_profile_pattern,
           }
        
    return render(request,'trade_admin_auth/changepattern.html', context)

def changeemailaddress(request,user_id):
    context={}
    user= User.objects.get(id=user_id)
    userprofile= AdminUser_Profile.objects.get(user=user.id)
    user_profile_id = userprofile.id
    user_decrypt_emailaddress =userprofile.emailaddress  
    decrypt_user_emailaddress=decrypt_with_common_cipher(user_decrypt_emailaddress)
    if request.method == 'POST':
       get_emailaddress = request.POST['emailaddress']
       if get_emailaddress != "":
          encrypt_useremail=encrypt_with_common_cipher(get_emailaddress)
          update_emailaddress = AdminUser_Profile.objects.get(id = user_profile_id)
          update_emailaddress.emailaddress = encrypt_useremail
          update_emailaddress.save()
          messages.add_message(request, messages.SUCCESS, 'Email address updated Successfully.')
          return HttpResponseRedirect('/tradeadmin/emailaddresschange/'+str(user_id)+'/')
       else:
          messages.add_message(request, messages.ERROR, 'Email address must required.')
          return HttpResponseRedirect('/tradeadmin/emailaddresschange/'+str(user_id)+'/')
    else:
        context={
            'Title':'Profile Setting',
            'decrypt_user_emailaddress':decrypt_user_emailaddress,
          }
    return render(request,'trade_admin_auth/changeemailaddress.html', context)

def admintwofaupdate(request):
    form = GoogleTokenVerificationForm()
    if request.method == 'POST':
        form = GoogleTokenVerificationForm(request.POST)
        if form.is_valid():
            token = request.POST['token']
            secertkey = request.POST['secertkey']
            authtoken = pyotp.TOTP(secertkey)
            verification = authtoken.now()
            msg=''
            if token == verification:
                uid =request.user.id
                try:
                    user = User.objects.get(pk=uid)
                    user_id = user.id
                    get_userprofile = AdminUser_Profile.objects.get(user = user_id)

                except User.DoesNotExist:
                    user = None
                    get_userprofile = None
                if user is not None and get_userprofile is not None:
                    if get_userprofile.twofa == False:
                        get_userprofile.twofa = True
                        get_userprofile.google_id = secertkey
                        get_userprofile.save()
                        msg='two factor authentication enabled successfully.'
                    elif get_userprofile.twofa == True:
                        get_userprofile.twofa = False
                        get_userprofile.google_id = secertkey 
                        get_userprofile.save()
                        msg='two factor authentication disabled successfully.'

                    messages.add_message(request, messages.SUCCESS, msg)
                    return HttpResponseRedirect('/tradeadmin/admin2fa/')
                else:
                   messages.add_message(request, messages.ERROR, 'Already status updated.')
                   return HttpResponseRedirect('/tradeadmin/admin2fa/')
            else:
                messages.add_message(request, messages.ERROR,'Invalid 2FA Code')
                return HttpResponseRedirect('/tradeadmin/admin2fa/')
        else:
           messages.add_message(request, messages.ERROR,form.errors)
           return HttpResponseRedirect('/tradeadmin/admin2fa/') 
    else:
        try:
          get_userprofile = AdminUser_Profile.objects.get(user = request.user.id)
        except AdminUser_Profile.DoesNotExist:
         get_userprofile  = ''
        secertkey =''
        if get_userprofile.google_id != None and get_userprofile.google_id !='':
          secertkey = get_userprofile.google_id
        else:
          secertkey = pyotp.random_base32()

        pytop =pyotp.totp.TOTP(secertkey).provisioning_uri(name=request.user.email, issuer_name='Global Experts')
        verification = pyotp.TOTP(secertkey)
        authtoken = verification.now()
        usertwofastatus = get_userprofile.twofa
        usersecertkey = ''
        if usertwofastatus == True:
          usersecertkey = get_userprofile.google_id
        else:
          usersecertkey = secertkey

        context ={
          'Title':'Two Factor Auth',
          'userpytop':pytop,
          'secertkey':usersecertkey,
          'get_userprofile':get_userprofile,
          'form5':GoogleTokenVerificationForm()

        }
    return render(request,'trade_admin_auth/enable2fa.html', context)

class ListUserAddress(ListView):
    model = UserAddress
    template_name = 'trade_admin_auth/generic_list.html'
    def get_queryset(self, **kwargs):
      return UserAddress.objects.all().order_by('-id')
    
    def get_context_data(self,**kwargs):
        context=super(ListUserAddress, self).get_context_data(**kwargs)
        context['Title'] = 'User Address List'
        content_qs = UserAddress.objects.all().order_by('-id')
        context['content_qs'] =content_qs
        contenttable = UserAddressTable(content_qs)
        context['table'] = contenttable
        context['activecls']='useraddressadmin'
        return context


class ListAdminactivity(SubAdminRequiredMixin,ListView):
    model = AdminUser_Activity
    template_name = 'trade_admin_auth/subadmin_activity_list.html'
    def get_queryset(self, **kwargs):
      return AdminUser_Activity.objects.filter(Q(user__admin_user_profile__role=1) | Q(user__admin_user_profile__role=0)).order_by('-id')
    def get_context_data(self,**kwargs):
        context=super(ListAdminactivity, self).get_context_data(**kwargs)
        context['Title'] = 'Admin Login History'
        tradeuser_qs = AdminUser_Activity.objects.filter(Q(user__admin_user_profile__role=1) | Q(user__admin_user_profile__role=0)).order_by('-id')
        filter = AdminActivityTableFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = AdminActivitySearch_Form()
        filter.form.helper.add_input(Submit('submit', 'Search',css_class="btn btn-default"))
        filter.form.helper.add_input(Reset('Reset Search','Reset Search',css_class="btn btn-default",css_id='reset-search'))
        contenttable = AdminActivityTable(filter.qs)
        context['tradeuser_qs'] =tradeuser_qs
        context['table'] = contenttable
        RequestConfig(self.request, paginate={'per_page': 15}).configure(contenttable)
        context['filter'] = filter
        context['Reset_url'] = 'trade_admin_auth:subadminactivity'
        context['activecls']='subdetailadmin'
        
        return context





