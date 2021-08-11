from django.contrib import admin
from cryptotoken.models import TokenDetails,RoadMap,CurrencyDetails,TokenInformation



admin.site.register(TokenDetails)
admin.site.register(RoadMap)
admin.site.register(CurrencyDetails)
admin.site.register(TokenInformation)