from django.forms import ModelForm
from django import forms


from django.forms import ModelChoiceField

from django.forms import widgets
from betterforms.multiform import MultiModelForm,MultiForm
from django.core.validators import MinValueValidator, MaxValueValidator
from collections import OrderedDict

from django.contrib.auth.models import User,Group

from cryptotoken.models import TokenDetails,RoadMap,CurrencyDetails,TokenInformation


class RoadMapForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40}),required=False)
    class Meta:
        model= RoadMap
        fields=['title','years','content','status']
        exclude=['created_on','modified_on','created_by','modified_by' ]


class TokenDetailsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40}),required=False)
    class Meta:
        model= TokenDetails
        fields=['name','symbol','platform','supply','teamwallet','presupply','liquidtypool','token_burn','presaleprice','pancakeswap','liquidity_lock','content','status']
        exclude=['created_on','modified_on','created_by','modified_by' ]

class CurrencyDetailsForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40}),required=False)
    class Meta:
        model= CurrencyDetails
        fields=[
        'name',
        'symbol',
        #'platform',
        #'supply',
        # 'reward_distributed',
        # 'charity',
        # 'marketing',
        # 'teamwallet',
        # 'teamwallet_duration',
        # 'presupply',
        # 'liquidtypool',
        # 'presaleprice',
        # 'pancakeswap',
        # 'token_burn',
        # 'blackholeaddress',
        # 'liquiditylock',
        'attachments',
        'timerdate',
        'content'
        ]
        exclude=['created_on','modified_on','created_by','modified_by','status' ]

class TokenInformationForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40}),required=False)
    class Meta:
        model= TokenInformation
        fields=['name','percentage','colour','content','status']
        exclude=['created_on','modified_on','created_by','modified_by','status' ]