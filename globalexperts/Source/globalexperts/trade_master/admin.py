from django.contrib import admin
from trade_master.models import Cms_StaticContent,Marketingvideo,Faq,Contactus,EmailTemplate,Testimonial,Blog
from auditable.views import AuditableAdminMixin

from trade_master.models import Subscribeuser,Newsletter

class Cms_StaticContentAdmin(AuditableAdminMixin):
    model = Cms_StaticContent
    list_display = ['id','name','title','content','status']
    
admin.site.register(Cms_StaticContent,Cms_StaticContentAdmin)
admin.site.register(Faq)
admin.site.register(Contactus)
admin.site.register(EmailTemplate)
admin.site.register(Testimonial)
admin.site.register(Subscribeuser)
admin.site.register(Newsletter)
admin.site.register(Blog)
admin.site.register(Marketingvideo)