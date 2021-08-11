from django.urls import include, path,re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView
from django.views.decorators.csrf import csrf_exempt
app_name = 'trade_auth'

from . import views

loginurl='/LELPMDfDsmez0ksi/'


urlpatterns = [

	re_path('aboutus', views.aboutus, name='aboutus'),
	re_path('whitepaper', views.whitepaper, name='whitepaper'),
	re_path('contactus', views.contactus, name='contactus'),
	re_path('buytoken', views.buytoken, name='buytoken'),
	re_path('ourteam', views.ourteam, name='ourteam'),
	re_path('faq', views.faq, name='faq'),
	re_path('privacy', views.privacy, name='privacy'),
	re_path('terms', views.terms, name='terms'),
	re_path('roadmap', views.roadmap, name='roadmap'),
	re_path('offline', views.offline_view, name='offline_view'),
	re_path('comingsoon', views.comingsoon_view, name='comingsoon'),
	re_path('walletdetails', views.walletdetails, name='walletdetails'),
	re_path('disconnectwallet', views.disconnectwallet, name='disconnectwallet'),
	re_path(r'^connectmetamask', csrf_exempt(views.connection_wallet), name='connectmetamask'),
	path('bloginfo/<int:id>/',views.info_blog,name='blogdetail'),
	re_path('blog', views.blog_list, name='blog'),
	path('markettingvideo/',views.video_list,name='markettingvideo'),
	
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)