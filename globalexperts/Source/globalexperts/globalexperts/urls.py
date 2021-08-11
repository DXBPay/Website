from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from trade_admin_auth.views import adminlogin
from trade_auth.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^global/',include("trade_auth.urls" ,namespace="trade_auth")),
    re_path(r'^tradeadmin/',include("trade_admin_auth.urls" ,namespace="trade_admin_auth")),
    re_path(r'^trademaster/',include("trade_master.urls" ,namespace="trade_master")),
    re_path(r'^token/',include("cryptotoken.urls" ,namespace="cryptotoken")),
    re_path(r'^support/',include("support.urls" ,namespace="support")),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path('LELPMDfDsmez0ksi', adminlogin, name='adminlogin'),
    re_path('', home, name='home'),
]
