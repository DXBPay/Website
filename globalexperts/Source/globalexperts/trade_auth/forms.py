from django.forms import ModelForm
from django import forms


from django.forms import ModelChoiceField

from django.forms import widgets
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User,Group
from company.models import Company,Company_Settings

from trade_admin_auth.models import AdminUser_Profile,User_Kyc_Verification
from trade_admin_auth.models import KYC_List
from betterforms.multiform import MultiModelForm,MultiForm
from django.core.validators import MinValueValidator, MaxValueValidator

from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,PasswordChangeForm
from locations.models import Country,State,Cities
from django.db.models import Q,F,Func,Value

from trade_master.models import Contactus

class Contactform(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),required = True)
    class Meta:
        model= Contactus
        fields='__all__'
        exclude=['created_on','modified_on','reply','status','read_status',]


    
