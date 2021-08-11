from django.forms import ModelForm
from django import forms


from django.forms import ModelChoiceField

from django.forms import widgets
from betterforms.multiform import MultiModelForm,MultiForm
from django.core.validators import MinValueValidator, MaxValueValidator
from collections import OrderedDict

from django.contrib.auth.models import User,Group
from company.models import Company,Company_Settings

from support.models import SupportCategory,SupportTicket,Newsletter,SupportTicketDetails





class SupportCategoryForm(forms.ModelForm):
    
    class Meta:
        model= SupportCategory
        fields=['name', 'status']
        exclude=['created_on','modified_on' ]



class SupportTicketForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 50}),required=True) 
    class Meta:
        model= SupportTicket
        fields=['category', 'subject','message','attachment']
        exclude=['created_on','modified_on','status' ]


class SupportTicketDetailAdminForm(forms.ModelForm):
    agree = forms.BooleanField(required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 70}),required=True,label='Reply Message') 
    class Meta:
        model= SupportTicketDetails
        fields=[ 'message','attachment']
        exclude=['created_on','modified_on','status' ]


class SupportTicketDetailForm(forms.ModelForm):
    agree = forms.BooleanField(required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}),required=True,label='Reply Message') 
    class Meta:
        model= SupportTicketDetails
        fields=[ 'message','attachment']
        exclude=['created_on','modified_on','status' ]

class NewsletterForm(forms.ModelForm):
    class Meta:
        model= Newsletter
        fields=['category', 'subject','message']
        exclude=['created_on','modified_on','status', ]