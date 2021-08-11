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



from django.db.models import Q,F,Func,Value
from django.db.models import Count, Min,Max, Sum, Avg,DecimalField,DateTimeField,CharField
from django.db.models.expressions import RawSQL
from django.db.models.functions import Cast,TruncSecond,ExtractSecond


from django.db import transaction

from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.contrib import messages


from trade_perms.mixins import OR_PermissionsRequiredMixin, shared_permission_access, admin_permission_access
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required,user_passes_test
from django.core.exceptions import PermissionDenied
from auditable.views import AuditableMixin


from django_ajax.decorators import ajax


from django_tables2 import RequestConfig



from django.template.loader import get_template
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives




from trade_admin_auth.mixins import check_group
from trade_admin_auth.mixins import CmsAdminRequiredMixin,FaqAdminRequiredMixin,ContactusAdminRequiredMixin
from trade_admin_auth.mixins import EmailTemplateAdminRequiredMixin



from trade_master.models import Cms_StaticContent,Faq,Contactus,Blog,Marketingvideo,EmailTemplate,Testimonial
from trade_master.forms import ContentPageForm,Blogpageform,videoform,FaqForm,ContactForm,EmailContentForm,TestimonialForm

from trade_master.tables import StaticContentTable,CmsContentTable,BlogTable,MarketingTable,FaqTable,ContactusTable
from trade_master.tables import EmailTemplateTable,TestimonialTable
from trade_auth.views import get_email_template,checkmessage,encrypt_with_common_cipher,decrypt_with_common_cipher


class Liststaticcontent(ListView):
    model = Cms_StaticContent
    template_name = 'trade_master/generic_list.html'
    def get_queryset(self, **kwargs):
      return Cms_StaticContent.objects.filter(contenttype=0)
    
    def get_context_data(self,**kwargs):
        context=super(Liststaticcontent, self).get_context_data(**kwargs)
        context['Title'] = 'CMS Page'
        content_qs = Cms_StaticContent.objects.filter(contenttype=0)
        context['content_qs'] =content_qs
        contenttable = StaticContentTable(content_qs)
        context['table'] = contenttable
        context['activecls']='cmsstaticadmin'
        return context



class UpdateCms_StaticContent(UpdateView):
    model = Cms_StaticContent
    form_class = ContentPageForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateCms_StaticContent, self).get_context_data(**kwargs)
       context['Title'] = 'Cms Page'
       context['Btn_url'] = 'trade_master:cmspagelist'
       context['activecls']='cmsstaticadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       form.instance.contenttype =0
       formsave=form.save()
       messages.add_message(self.request, messages.SUCCESS, 'cms page updated successfully.')
       return HttpResponseRedirect('/trademaster/cmspagelist/')


class DetailStaticcontent(DetailView):
    model = Cms_StaticContent 
    template_name = 'trade_master/cms_detail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailStaticcontent, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Cms_StaticContent.objects.get(id=p_key)
       context['Title'] = 'Cms Page Detail'
       context['staticcontent_qs']=staticcontent_qs
       context['activecls']='cmsstaticadmin'
       return context

class Listcontent(ListView):
    model = Cms_StaticContent
    template_name = 'trade_master/generic_list.html'
    def get_queryset(self, **kwargs):
      return Cms_StaticContent.objects.filter(contenttype=1)
    
    def get_context_data(self,**kwargs):
        context=super(Listcontent, self).get_context_data(**kwargs)
        context['Title'] = 'CMS Home Content'
        content_qs = Cms_StaticContent.objects.filter(contenttype=1)
        context['content_qs'] =content_qs
        contenttable = CmsContentTable(content_qs)
        context['table'] = contenttable
        context['activecls']='cmsstaticadmin'
        return context



class UpdateCms_Content(UpdateView):
    model = Cms_StaticContent
    form_class = ContentPageForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateCms_Content, self).get_context_data(**kwargs)
       context['Title'] = 'Cms Home Content'
       context['Btn_url'] = 'trade_master:cmspagecontentlist'
       context['activecls']='cmsstaticadmin'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       form.instance.contenttype =1
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'cms content updated successfully.')
       return HttpResponseRedirect('/trademaster/cmspagecontentlist/')

class Blog_list(ListView):
  model = Blog
  template_name = 'trade_master/blog_list.html'
  def get_queryset(self, **kwargs):
      return Blog.objects.all().order_by('-id')
    
  def get_context_data(self,**kwargs):
    context=super(Blog_list, self).get_context_data(**kwargs)
    context['Title'] = 'Blog List'
    content_qs = Blog.objects.all().order_by('-id')
    context['content_qs'] =content_qs
    contenttable = BlogTable(content_qs)
    context['add_title'] ='Add Blog'
    context['Btn_url'] = 'trade_master:addblog'
    context['table'] = contenttable
    return context

class DetailBlog(DetailView):
    model = Blog 
    template_name = 'trade_master/blog_detail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailBlog, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Blog.objects.get(id=p_key)
       context['Title'] = 'Blog Detail'
       context['staticcontent_qs']=staticcontent_qs
       return context


class UpdateBlogcontent(UpdateView):
    model = Blog
    form_class = Blogpageform
    template_name = 'trade_master/blogupdate_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateBlogcontent, self).get_context_data(**kwargs)
       context['Title'] = 'Blog Update'
       context['Btn_url'] = 'trade_master:bloglist'
       return context
    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()
       messages.add_message(self.request, messages.SUCCESS, 'Blog Detail Updated Successfully.')
       return HttpResponseRedirect('/trademaster/bloglist/')

class AddBlog(CreateView):
    model = Faq
    form_class = Blogpageform
    template_name = 'trade_master/blogupdate_form.html'   
    def get_context_data(self, **kwargs):
      context = super(AddBlog, self).get_context_data(**kwargs)
      context['Title'] = 'Add Blog'
      context['Btn_url'] = 'trade_master:bloglist'
      return context
    @transaction.atomic
    def form_valid(self, form):
      form.instance.created_by_id = self.request.user.id
      form.instance.modified_by_id = self.request.user.id
      formsave=form.save()
      messages.add_message(self.request, messages.SUCCESS, 'Blog Created Successfully.')
      return HttpResponseRedirect('/trademaster/bloglist/')


class Marketingvideo_list(ListView):
  model = Marketingvideo
  template_name = 'trade_master/marketingvideolist.html'
  def get_queryset(self, **kwargs):
      return Marketingvideo.objects.all().order_by('-id')
  def get_context_data(self,**kwargs):
    context=super(Marketingvideo_list, self).get_context_data(**kwargs)
    context['Title'] = 'Marketingvideo'
    content_qs = Marketingvideo.objects.all().order_by('-id')
    context['content_qs'] =content_qs
    contenttable = MarketingTable(content_qs)
    context['add_title'] ='Add Blog'
    context['table'] = contenttable
    return context

class Updatevideo(UpdateView):
    model = Marketingvideo
    form_class = videoform
    template_name = 'trade_master/videoupdate_form.html'   
    def get_context_data(self, **kwargs):
       context = super(Updatevideo, self).get_context_data(**kwargs)
       context['Title'] = 'video Update'
       context['Btn_url'] = 'trade_master:videolist'
       return context
    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()
       messages.add_message(self.request, messages.SUCCESS, 'Video Detail Updated Successfully.')
       return HttpResponseRedirect('/trademaster/videolist/')


class Detailcontent(DetailView):
    model = Cms_StaticContent 
    template_name = 'trade_master/cms_content_detail.html'
    def get_context_data(self, **kwargs):
       context = super(Detailcontent, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Cms_StaticContent.objects.get(id=p_key)
       context['Title'] = 'Cms Home Content Detail'
       context['staticcontent_qs']=staticcontent_qs
       context['activecls']='cmsstaticadmin'
       return context

class AddTestimonial(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(AddTestimonial, self).get_context_data(**kwargs)
       context['Title'] = 'Add Our Team'
       context['Btn_url'] = 'trade_master:testimoniallist'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'team created successfully.')
       return HttpResponseRedirect('/trademaster/testimoniallist/')

class ListTestimonial(ListView):
    model = Testimonial
    template_name = 'trade_master/generic_list_add.html'
    def get_queryset(self, **kwargs):
      return Testimonial.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListTestimonial, self).get_context_data(**kwargs)
        context['Title'] = 'Our Team List'
        content_qs = Testimonial.objects.all()
        context['content_qs'] =content_qs
        contenttable = TestimonialTable(content_qs)
        context['table'] = contenttable
        context['add_title'] ='Add Our Team'
        context['Btn_url'] = 'trade_master:addtestimonial'

        return context

class UpdateTestimonial(UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateTestimonial, self).get_context_data(**kwargs)
       context['Title'] = 'Edit Our Team '
       context['Btn_url'] = 'trade_master:testimoniallist'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'testimonial updated successfully.')
       return HttpResponseRedirect('/trademaster/testimoniallist/')

class DetailTestimonial(DetailView):
    model = Testimonial 
    template_name = 'trade_master/testimonialdetail.html'
    def get_context_data(self, **kwargs):
       context = super(DetailTestimonial, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Testimonial.objects.get(id=p_key)
       context['Title'] = 'Our Team Detail'
       context['staticcontent_qs']=staticcontent_qs
       return context


class ListFaq(ListView):
    model = Faq
    template_name = 'trade_master/generic_list_add.html'
    def get_queryset(self, **kwargs):
      return Faq.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListFaq, self).get_context_data(**kwargs)
        context['Title'] = 'FAQ'
        content_qs = Faq.objects.all()
        context['content_qs'] =content_qs
        contenttable = FaqTable(content_qs)
        context['table'] = contenttable
        context['add_title'] ='Add FAQ'
        context['Btn_url'] = 'trade_master:addfaq'
        return context

class AddFaq(CreateView):
    model = Faq
    form_class = FaqForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(AddFaq, self).get_context_data(**kwargs)
       context['Title'] = 'Add FAQ'
       context['Btn_url'] = 'trade_master:faqlist'
       return context

    @transaction.atomic
    def form_valid(self, form):
        
       form.instance.created_on   = datetime.datetime.now()
       form.instance.created_by_id = self.request.user.id
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'faq created successfully.')
       return HttpResponseRedirect('/trademaster/faqlist/')

class UpdateFaq(UpdateView):
    model = Faq
    form_class = FaqForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateFaq, self).get_context_data(**kwargs)
       context['Title'] = 'Update FAQ'
       context['Btn_url'] = 'trade_master:faqlist'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.modified_by_id = self.request.user.id
       formsave=form.save()

       messages.add_message(self.request, messages.SUCCESS, 'faq updated successfully.')
       return HttpResponseRedirect('/trademaster/faqlist/')


class Detailfaq(DetailView):
    model = Faq 
    template_name = 'trade_master/faq_detail.html'
    def get_context_data(self, **kwargs):
       context = super(Detailfaq, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Faq.objects.get(id=p_key)
       context['Title'] = 'FAQ Detail'
       context['staticcontent_qs']=staticcontent_qs
       return context



class Listcontactus(ListView):
    model = Contactus
    template_name = 'trade_master/generic_list.html'
    def get_queryset(self, **kwargs):
      return Contactus.objects.filter(status=0).order_by('-id')
    
    def get_context_data(self,**kwargs):
        context=super(Listcontactus, self).get_context_data(**kwargs)
        context['Title'] = 'Contacted User List'
        content_qs = Contactus.objects.filter(status=0).order_by('-id')
        context['content_qs'] =content_qs
        contenttable = ContactusTable(content_qs)
        context['table'] = contenttable
        return context


class UpdateContactus(UpdateView):
    model = Contactus
    form_class = ContactForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(UpdateContactus, self).get_context_data(**kwargs)
       context['Title'] = 'Update Contact user'
       context['Btn_url'] = 'trade_master:contactlist'
       return context

    @transaction.atomic
    def form_valid(self, form):
       form.instance.read_status = 1
       formsave=form.save()
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
       email_template = EmailTemplate.objects.get(id = 2)
       if email_template:
          email_template_qs =email_template
       else:
          email_template_qs = ''

       text_file = open("trade_master/templates/emailtemplate/contactus_reply.html", "w")  
       text_file.write(email_template.content)
       text_file.close()
       email_subject = email_template.Subject
       to_email = formsave.email
       from_email_get = settings.EMAIL_USER
       from_email =decrypt_with_common_cipher(from_email_get)
       currentYear = datetime.datetime.now().year
       hostuser= decrypt_with_common_cipher(settings.EMAIL_HOST_US)
       hostpwd=decrypt_with_common_cipher(settings.EMAIL_PASSWORD)
       settings.EMAIL_HOST_PASSWORD = hostpwd
       settings.EMAIL_HOST_USER = hostuser
       data= {
          'username':formsave.name,
          'email':to_email,
          'company_logo':'comp_company_logo',
          'reply': formsave.reply,
          'company_name':companyname,
          'years':currentYear,
          'fb':companyfb,
          'twitter':companytwitter
          }
       text_content = 'This is an important message.'
       htmly = get_template('emailtemplate/contactus_reply.html')
       html_content = htmly.render(data)
       msg = EmailMultiAlternatives(email_subject, text_content, from_email, [to_email])
       msg.attach_alternative(html_content, "text/html")
       msg.send()

       messages.add_message(self.request, messages.SUCCESS, 'reply message updated successfully.')
       return HttpResponseRedirect('/trademaster/contactlist/')


class Detailcontactus(DetailView):
    model = Contactus 
    template_name = 'trade_master/contactus_detail.html'
    def get_context_data(self, **kwargs):
       context = super(Detailcontactus, self).get_context_data(**kwargs)
       p_key = int(self.kwargs['pk'])
       staticcontent_qs = Contactus.objects.get(id=p_key)
       context['Title'] = 'Contact Info'
       context['staticcontent_qs']=staticcontent_qs
       return context





class Listemailcontent(ListView):
    model = EmailTemplate
    template_name = 'trade_master/generic_list.html'
    def get_queryset(self, **kwargs):
      return EmailTemplate.objects.filter(status=0)
    
    def get_context_data(self,**kwargs):
        context=super(Listemailcontent, self).get_context_data(**kwargs)
        context['Title'] = 'Email Template List'
        content_qs = EmailTemplate.objects.filter(status=0)
        context['content_qs'] =content_qs
        contenttable = EmailTemplateTable(content_qs)
        context['table'] = contenttable
        return context

class Updateemailcontenttemplate(UpdateView):
    model = EmailTemplate
    form_class = EmailContentForm
    template_name = 'trade_master/generic_form.html'   
    def get_context_data(self, **kwargs):
       context = super(Updateemailcontenttemplate, self).get_context_data(**kwargs)
       context['Title'] = 'Update Email Template'
       context['Btn_url'] = 'trade_master:emailcontactlist'
       return context
    @transaction.atomic
    def form_valid(self, form):
       formsave=form.save()
       messages.add_message(self.request, messages.SUCCESS, 'email content updated successfully.')
       return HttpResponseRedirect('/trademaster/emailcontactlist/')


