from django.contrib import admin
from modules.models import MenuModules




class ModulesPermissionsAdmin(admin.ModelAdmin):
    model = MenuModules
    list_display = ['id','module_code','module_name','status']
    
admin.site.register(MenuModules,ModulesPermissionsAdmin)