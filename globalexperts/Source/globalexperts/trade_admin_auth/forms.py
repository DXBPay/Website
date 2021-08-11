from django.forms import ModelForm
from django import forms


from django.forms import ModelChoiceField

from django.forms import widgets
from django.core.exceptions import ValidationError

from django.contrib.auth.models import User,Group
from company.models import Company,Company_Settings
from trade_admin_auth.models import AdminUser_Profile,MenuPermissions,User_Kyc_Verification



from betterforms.multiform import MultiModelForm,MultiForm
from django.core.validators import MinValueValidator, MaxValueValidator
from collections import OrderedDict
from django.contrib.auth.forms import UserCreationForm



class EditCompanyForm(forms.ModelForm):
    gplus = forms.CharField(required=True,label="Telegram") 
    class Meta:
        model= Company
        
        fields=['name','email','company_logo','company_fav','copy_right','gplus','fb','twitter','linkedin','instagram','address1','phone1','social1','social2','social3']

        exclude=['created_on','modified_on','state','trade_percentage','admin_redirect','city','country','postcode','company_video']

class EditCompanySettingsForm(forms.ModelForm):
    
    site_maintenance = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}),required = False,label='Coming Soon Message')
    depositurl = forms.CharField(label='Marketing Video URL One')
    withdrawurl = forms.CharField(label='Marketing Video URL Two')
    coinmarket = forms.CharField(label='Marketing Video URL Three')
    class Meta:
        model= Company_Settings
        
        fields=['site_maintenance_status','adminipaddress','depositurl','withdrawurl','coinmarket','coingecko','new_coin_status','site_maintenance']

        exclude=['company_settings_name','free_days','margin_percentage','lending_percentage','free_bonus_status','bonus_amount','base_price_percenatge','fees_amount']


class EditCompanyMultiForm(MultiModelForm):
    
    form_classes = {
        'form1': EditCompanyForm,
        'form2': EditCompanySettingsForm,
    }


class AdminUserAddForm(UserCreationForm):
    email = forms.CharField(required = True)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        print (User.objects.filter(email=email).count())
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email

    class Meta:
        model= User
        fields=['username', 'email','password1', 'password2',]
        exclude=['is_staff','first_name', 'last_name', ]

    


class AdminUserProfileAddform(forms.ModelForm):
  
    pattern_code = forms.CharField(initial='',widget=forms.widgets.HiddenInput(),required=True)
    class Meta:
        model= AdminUser_Profile
        fields='__all__'
        exclude=['created_on','modified_on','user','state','role','address1',
        'address2','date_of_birth','referal_status','referal_code','refer_by_id','referal_user_by','status',
        'gender','phone1','photo','city','country','postcode','country_code','google_id'
        ]


class AdminUserAddMultiForm(MultiModelForm):
    form_classes = {
        'form1': AdminUserAddForm,
        'form2': AdminUserProfileAddform,
        
        }

class AdminUserEditsubForm(UserCreationForm):
    email = forms.CharField(required = True)
    
    

    class Meta:
        model= User
        fields=['username', 'email','password1', 'password2',]
        exclude=['is_staff','first_name', 'last_name', ]
class AdminSubadmineditform(forms.ModelForm):
  
    
    class Meta:
        model= AdminUser_Profile
        fields='__all__'
        exclude=['created_on','modified_on','user','state','role','address1',
        'address2','date_of_birth','referal_status','referal_code','refer_by_id','referal_user_by','status',
        'gender','phone1','photo','city','country','postcode','country_code','google_id'
        ]

class AdminUserEditSubadminMultiForm(MultiModelForm):
    form_classes = {
        'form1': AdminUserEditsubForm,
        'form2': AdminSubadmineditform,
        
        }

class AdminMenuPermissionForm(forms.ModelForm):

    class Meta:
        model= MenuPermissions
        fields='__all__'
        exclude=['created_on','modified_on','user_permissions']


class AdminUserProfileeditform(forms.ModelForm):
  
    
    class Meta:
        model= AdminUser_Profile
        fields='__all__'
        exclude=['created_on','modified_on','user','state','role',
        'address2','date_of_birth','refer_id','refer_user_id','refer_by_id','activation_date','pattern_code'
        ,'gender','phone1','address1','city','country','postcode','photo','list_country','country_code','authy_id','google_id'
        ]


class AdminUserEditForm(forms.ModelForm):
    email = forms.CharField(required = True)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        print (User.objects.filter(email=email).count())
        if email and User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u'This email address is already registered.')
        return email
    class Meta:
        model= User
        fields=['email']
        exclude=['is_staff','first_name', 'last_name','password1', 'password2','username',]

class AdminUserEditMultiForm(MultiModelForm):
    form_classes = {
        'form1': AdminUserEditForm,
        'form2': AdminUserProfileeditform,
        
        }


class KycupdateForm(forms.ModelForm):

    class Meta:
        model= User_Kyc_Verification
        fields='__all__'
        exclude=['created_on','modified_on','user_kyc']


class ChangePatternForm(forms.ModelForm):

    pattern_code = forms.CharField(initial=0,widget=forms.widgets.HiddenInput())
    class Meta:
        model= AdminUser_Profile
        fields='__all__'
        exclude=['created_on','modified_on','user','state','role',
        'address2','date_of_birth','refer_id','refer_user_id','refer_by_id','activation_date',
        'address1','city','country','postcode','phone1','gender','photo','country_code','authy_id','google_id'
        ]

class GoogleTokenVerificationForm(forms.Form):
    token = forms.CharField(required=True,label='TwoFA Code')
