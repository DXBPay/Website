from django.contrib import admin

from company.models import Company,Company_Branches,Company_Settings


admin.site.register(Company)
admin.site.register(Company_Branches)
admin.site.register(Company_Settings)

