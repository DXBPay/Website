from django.forms import ModelForm
from django import forms


from django.forms import ModelChoiceField

from django.forms import widgets
from betterforms.multiform import MultiModelForm,MultiForm
from django.core.validators import MinValueValidator, MaxValueValidator
from collections import OrderedDict

from django.contrib.auth.models import User,Group
from company.models import Company,Company_Settings

from trade_master.models import Cms_StaticContent,Faq,Blog,Marketingvideo,Contactus,EmailTemplate,Testimonial




class TestimonialForm(forms.ModelForm):
    
    class Meta:
        model= Testimonial
        fields=['name', 'location','photo']
        exclude=['created_on','modified_on','status','content' ]

class ContentPageForm(forms.ModelForm):
    
    class Meta:
        model= Cms_StaticContent
        fields=['title', 'content']
        exclude=['name','contenttype','created_on','modified_on','status' ]


class Blogpageform(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['blogtitle','blogimage','blogcontent','blogsubject','status']
        exclude = ['created_on','modified_on']


class videoform(forms.ModelForm):
    class Meta:
        model = Marketingvideo
        fields = ['videotitle','videourl','status']
        exclude = ['created_on','modified_on']



class FaqForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40}),required=True)
    class Meta:
        model= Faq
        fields=['title', 'content','status']
        exclude=['created_on','modified_on' ]

class ContactForm(forms.ModelForm):
    reply = forms.CharField(widget=forms.Textarea(attrs={"rows":4, "cols":40}),required=True)
    class Meta:
        model= Contactus
        fields=['reply',]
        exclude=['created_on','modified_on' ,'phone1','name','email','subject','message','read_status']

class EmailContentForm(forms.ModelForm):
    
    class Meta:
        model= EmailTemplate
        fields=['name', 'Subject','content']
        exclude=['created_on','modified_on' ]


