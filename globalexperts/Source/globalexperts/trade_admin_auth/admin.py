from django.contrib import admin
from django import forms
from django.db import models

from trade_admin_auth.models import AdminUser_Profile,MenuPermissions,AdminUser_Activity
from trade_admin_auth.models import User_Kyc_Verification,User_Notification
from auditable.views import AuditableAdminMixin

class MenuPermissionsAdmin(AuditableAdminMixin):
    model = MenuPermissions
    list_display = ['user_permissions','access_modules','access_permissions']
    exclude=['created_by','modified_by']
class trade_admin_authAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ImageField: {'widget': forms.FileInput },
    }

admin.site.register(AdminUser_Profile)
admin.site.register(MenuPermissions,MenuPermissionsAdmin)
admin.site.register(AdminUser_Activity)
admin.site.register(User_Kyc_Verification)
admin.site.register(User_Notification)

