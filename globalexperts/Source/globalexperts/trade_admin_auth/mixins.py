from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import permission_required,user_passes_test

from django.http.response import HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.urls import reverse
from django.contrib import auth

from functools import wraps
from django.db.models import Q,F,Func,Value

from trade_admin_auth.models import MenuPermissions
from modules.models import MenuModules
from django.contrib.auth.models import User,Group
from company.models import Company,Company_Settings


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def get_browser_type(request):
    browser_with_version = request.user_agent.browser.family+' '+request.user_agent.browser.version_string
    return browser_with_version

def get_browser_os_type(request):
    browser_os_type = request.user_agent.os.family
    return browser_os_type
def get_browser_device_type(request):
    return request.user_agent.device.family


def allow_by_ip(view_func):
    try:
        companyqs = Company.objects.get(id=1)
        companyname= companyqs.name
        companyipaddress = companyqs.company_settings.adminipaddress
                
    except Company.DoesNotExist:
        companyqs = 'Global Experts'
        companyname = 'Global Experts'
        companyipaddress = ''
    def authorize(request, *args, **kwargs):
        user_ip = request.META.get('REMOTE_ADDR')
        if companyipaddress:
            if companyipaddress==user_ip:
                return view_func(request, *args, **kwargs)
        return HttpResponse('Invalid Ip Access!')
    return authorize



def check_adminip(group_name):
    def _check_adminip(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                companyqs = Company.objects.get(id=1)
                companyname= companyqs.name
                companyipaddress = companyqs.company_settings.adminipaddress
                
            except Company.DoesNotExist:
                companyqs = 'Global Experts'
                companyname = 'Global Experts'
                companyipaddress = ''
            user_ip = get_client_ip(request)
            if companyipaddress is not None and companyipaddress != '':
                if companyipaddress != user_ip:
                    auth.logout(request)
                    return HttpResponseRedirect('/tradeadmin/ipblock404/')
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_adminip


class CheckIpaddressAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        try:
            companyqs = Company.objects.get(id=1)
            companyname= companyqs.name
            companyipaddress = companyqs.company_settings.adminipaddress
            
        except Company.DoesNotExist:
            companyqs = 'Global Experts'
            companyname = 'Global Experts'
            companyipaddress = ''
        user_ip = get_client_ip(request)

        if companyipaddress is not None and companyipaddress != '':
            if companyipaddress != user_ip:
                auth.logout(request)
                return HttpResponseRedirect('/tradeadmin/ipblock404/')
            else:
                return super().dispatch(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)



def check_group(group_name):
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user_id =request.user.id
            get_groupname = MenuModules.objects.get(module_code=group_name)
            checkpermission = MenuPermissions.objects.filter(Q(access_modules=get_groupname.id) & Q(user_permissions=user_id))
            if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=get_groupname.id) & Q(access_permissions=0)).exists())
               ):
                return HttpResponseRedirect('/tradeadmin/page_403/')
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group





    
class SubAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=15) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')



class CmsAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=6) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')

class FaqAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=4) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')


class ContactusAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=2) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')


class EmailTemplateAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=5) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')



class ManageUserAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=1) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')



class ManageCurrencyAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=13) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')

class ManageReferalAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=16) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')

class ManageTicketSupportAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=7) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')
class ManageTradeAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=10) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')

class ManagePaymentAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=11) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')


class ManagePlanAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=17) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')

class ManageGenerationAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=18) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')


class ManageNewsletterAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=11) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')

class ManageBlockipAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=8) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')


class ManageBankDetailsAdminRequiredMixin:

    def dispatch(self, request, *args, **kwargs):        
        user_id =request.user.id
        if ((request.user.admin_user_menupermissions.filter(Q(user_permissions=user_id) & Q(access_modules=19) & (Q(access_permissions=1) | Q (access_permissions=2))).exists())):
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/tradeadmin/page_403/')