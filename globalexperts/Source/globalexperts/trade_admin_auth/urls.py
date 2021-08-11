from django.urls import include, path,re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
app_name = 'trade_admin_auth'

from . import views
from .views import EditCompanySetting,EditProfileSetting,ChangePasswordView,ListUserAddress

loginurl='/LELPMDfDsmez0ksi/'

urlpatterns = [

	 
	 re_path('admin_auth', views.adminlogin_auth, name='admin_auth'),
	 re_path('logout',    login_required(views.log_out,login_url=loginurl), name='logout'),
	 re_path('dashboard',    login_required(views.dashboard,login_url=loginurl), name='dashboard'),
	 re_path('adminforgotpassword', views.adminforgotpassword, name='adminforgotpassword'),
	 re_path(r'^general_settings/(?P<pk>[-\w]+)/$', login_required(views.EditCompanySetting.as_view(),login_url=loginurl), name='general_settings'),
	 re_path(r'^profile_settings/(?P<pk>[-\w]+)/$', login_required(views.EditProfileSetting.as_view(),login_url=loginurl), name='profile_settings'),
	 re_path(r'^change_password/$', login_required(ChangePasswordView.as_view(),login_url=loginurl), name='change_password'),
	 re_path(r'^patternchange/(?P<user_id>[-\w]+)/$', login_required(views.change_pattern_view,login_url=loginurl), name='patternchange'),
	 re_path(r'^emailaddresschange/(?P<user_id>[-\w]+)/$', login_required(views.changeemailaddress,login_url=loginurl), name='emailaddresschange'),
	 re_path('admin2fa', login_required(views.admintwofaupdate,login_url=loginurl), name='admin2fa'),
	 re_path(r'^twofaadmin/(?P<uid>[-\w]+)', views.admintwofa, name='twofaadmin'),
	 re_path(r'^useraddresslist/$', login_required(ListUserAddress.as_view(),login_url=loginurl), name='useraddresslist'),
	 
	 re_path(r'^page_403', views.Page403View, name='page_403'),
	 re_path(r'^page_404', views.Page404View, name='page_404'),
	 re_path(r'^page_500', views.Page500View, name='page_500'),
	 re_path(r'^ipblock404', views.IPBlock404View, name='ipblock404'),

	

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)