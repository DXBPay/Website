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
import decimal
from decimal import *
import json

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


from django_tables2 import RequestConfig
from crispy_forms.layout import Submit,ButtonHolder,Reset

from cryptotoken.models import TokenDetails,RoadMap,CurrencyDetails,TokenInformation
from cryptotoken.forms import RoadMapForm,TokenDetailsForm,CurrencyDetailsForm,TokenInformationForm
from cryptotoken.tables import RoadMapTable,CurrencyDetailsTable,TokenInformationTable

class ListRoadMap(ListView):
    model = RoadMap
    template_name = 'cryptotoken/generic_list_add.html'
    def get_queryset(self, **kwargs):
      return RoadMap.objects.all().order_by('id')
    
    def get_context_data(self,**kwargs):
        context=super(ListRoadMap, self).get_context_data(**kwargs)
        context['Title'] = 'Road Map List'
        content_qs = RoadMap.objects.all().order_by('id')
        context['content_qs'] =content_qs
        contenttable = RoadMapTable(content_qs)
        context['table'] = contenttable
        context['activecls']='cryptotokenadmin'
        context['Btn_url'] = 'cryptotoken:roadmapadd'
        context['add_title'] ='Add Road Map'
        return context

class AddRoadMap(CreateView):
    model = RoadMap
    form_class = RoadMapForm
    template_name = 'cryptotoken/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(AddRoadMap, self).get_context_data(**kwargs)
       context['Title'] = 'Add Road Map'
       context['Btn_url']='cryptotoken:roadmaplist'
       context['activecls']='cryptotokenadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'RoadMap created successfully.')
       return HttpResponseRedirect('/token/roadmaplist/')

class UpdateRoadMap(UpdateView):
    model = RoadMap
    form_class = RoadMapForm
    template_name = 'cryptotoken/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateRoadMap, self).get_context_data(**kwargs)
       context['Title'] = 'Edit Road Map'
       context['Btn_url']='cryptotoken:roadmaplist'
       context['activecls']='cryptotokenadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'RoadMap updated successfully.')
       return HttpResponseRedirect('/token/roadmaplist/')

class DetailRoadMap(DetailView):
    model = RoadMap 
    template_name = 'cryptotoken/roadmap_detail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailRoadMap, self).get_context_data(**kwargs)
       p_key = self.kwargs['pk']
       roadmap_qs = RoadMap.objects.get(id=p_key)
       context['Title'] = 'Road Map Detail'
       context['roadmapdetail']=roadmap_qs
       context['Btn_url'] = 'cryptotoken:roadmaplist'
       context['activecls']='cryptotokenadmin'
       return context


class ChangeTokenDetailView(UpdateView):
    model= TokenDetails
    template_name = 'cryptotoken/generic_form.html'
    form_class = TokenDetailsForm
   
    def get_context_data(self, **kwargs):
       context = super(ChangeTokenDetailView, self).get_context_data(**kwargs)
       context['Title']='Token Setting'
       return context
    @transaction.atomic
    def form_valid(self, form):
        formsave=form.save()
        messages.add_message(self.request, messages.SUCCESS, 'Token Detail Updated Successfully.')
        return HttpResponseRedirect(reverse('cryptotoken:tokensetting',kwargs={'pk': formsave.id}))
        


class ListCurrencyDetails(ListView):
    model = CurrencyDetails
    template_name = 'cryptotoken/generic_list.html'
    def get_queryset(self, **kwargs):
      return CurrencyDetails.objects.all().order_by('id')
    
    def get_context_data(self,**kwargs):
        context=super(ListCurrencyDetails, self).get_context_data(**kwargs)
        context['Title'] = 'Token Settings'
        content_qs = CurrencyDetails.objects.all().order_by('id')
        context['content_qs'] =content_qs
        contenttable = CurrencyDetailsTable(content_qs)
        context['table'] = contenttable
        context['activecls']='cryptotokenadmin'
        return context


class UpdateCurrencyDetail(UpdateView):
    model = CurrencyDetails
    form_class = CurrencyDetailsForm
    template_name = 'cryptotoken/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateCurrencyDetail, self).get_context_data(**kwargs)
       context['Title'] = 'Edit Token Settings'
       context['Btn_url']='cryptotoken:currencylist'
       context['activecls']='cryptotokenadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'Token Economics details updated successfully.')
       return HttpResponseRedirect('/token/currencylist/')


class DetailCurrencyDetail(DetailView):
    model = CurrencyDetails 
    template_name = 'cryptotoken/currencydetail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailCurrencyDetail, self).get_context_data(**kwargs)
       p_key = self.kwargs['pk']
       currencyqs = CurrencyDetails.objects.get(id=p_key)
       context['Title'] = 'Token Setting Detail'
       context['roadmapdetail']=currencyqs
       context['Btn_url'] = 'cryptotoken:currencylist'
       context['activecls']='cryptotokenadmin'
       return context


class ListTokenInformations(ListView):
    model = TokenInformation
    template_name = 'cryptotoken/generic_list_add.html'
    def get_queryset(self, **kwargs):
      return TokenInformation.objects.all().order_by('id')
    
    def get_context_data(self,**kwargs):
        context=super(ListTokenInformations, self).get_context_data(**kwargs)
        context['Title'] = 'Token List'
        content_qs = TokenInformation.objects.all().order_by('id')
        context['content_qs'] =content_qs
        contenttable = TokenInformationTable(content_qs)
        context['table'] = contenttable
        context['activecls']='cryptotokenadmin'
        context['Btn_url'] = 'cryptotoken:tokenadd'
        context['add_title'] ='Add Token'
        return context

class AddTokenInformations(CreateView):
    model = TokenInformation
    form_class = TokenInformationForm
    template_name = 'cryptotoken/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(AddTokenInformations, self).get_context_data(**kwargs)
       context['Title'] = 'Add Token'
       context['Btn_url']='cryptotoken:tokenlist'
       context['activecls']='cryptotokenadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'Token details added successfully.')
       return HttpResponseRedirect('/token/tokenlist/')

class UpdateTokenInformations(UpdateView):
    model = TokenInformation
    form_class = TokenInformationForm
    template_name = 'cryptotoken/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateTokenInformations, self).get_context_data(**kwargs)
       context['Title'] = 'Edit Token'
       context['Btn_url']='cryptotoken:tokenlist'
       context['activecls']='cryptotokenadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'Token details updated successfully.')
       return HttpResponseRedirect('/token/tokenlist/')


class DetailToken(DetailView):
    model = TokenInformation 
    template_name = 'cryptotoken/tokendetail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailToken, self).get_context_data(**kwargs)
       p_key = self.kwargs['pk']
       currencyqs = TokenInformation.objects.get(id=p_key)
       context['Title'] = 'Token Detail'
       context['roadmapdetail']=currencyqs
       context['Btn_url'] = 'cryptotoken:tokenlist'
       context['activecls']='cryptotokenadmin'
       return context