from django.contrib import admin
from support.models import Newsletter,SubscribeUser,NewsletterSubscribeUser
from support.models import SupportCategory,SupportTicket


admin.site.register(Newsletter)

admin.site.register(SubscribeUser)

admin.site.register(NewsletterSubscribeUser)

admin.site.register(SupportCategory)

admin.site.register(SupportTicket)