from django.urls import include, path,re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView
app_name = 'support'

loginurl='/W8n9cQU3MAh1mjhT/'

from . import views
from .views import AddSupportCategory,ListSupportCategory,UpdateSupportCategory
from .views import  ListSupportTicket,UpdateSupportTicket,DetailSupportticket,AddNewsletter,ListNewsletter,DetailNewsletter
from .views import ListSubscribeUserAdmin,DeleteSubscribeuser,AddSupportView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [

	 

	
	re_path(r'^updatesupportcategory/(?P<pk>[-\w]+)/$', login_required(UpdateSupportCategory.as_view(),login_url=loginurl), name='updatesupportcategory'),
	re_path(r'^supportcategorylist/$', login_required(ListSupportCategory.as_view(),login_url=loginurl), name='supportcategorylist'), 
	re_path(r'^addsupportcategory/$', login_required(AddSupportCategory.as_view(),login_url=loginurl), name='addsupportcategory'),
	
	re_path(r'^updatesupportticket/(?P<pk>[-\w]+)/$', login_required(UpdateSupportCategory.as_view(),login_url=loginurl), name='updatesupportticket'),
	re_path(r'^ticketsupportlist/$', login_required(ListSupportTicket.as_view(),login_url=loginurl), name='ticketsupportlist'), 
	re_path(r'^detail_supportticket/(?P<supportid>[-\w]+)/$', login_required(views.supportreply_view,login_url=loginurl), name='detail_supportticket'),

	re_path(r'^addnewsletter/$', login_required(AddNewsletter.as_view(),login_url=loginurl), name='addnewsletter'),
	re_path(r'^listnewsletter/$', login_required(ListNewsletter.as_view(),login_url=loginurl), name='listnewsletter'),
	re_path(r'^newsletterdetail/(?P<pk>[-\w]+)/$', login_required(DetailNewsletter.as_view(),login_url=loginurl), name='newsletterdetail'),

	re_path(r'^newsletter_add/$', login_required(views.newsletter_add,login_url=loginurl), name='newsletter_add'),
	re_path(r'^subscribedetail/(?P<pk>[-\w]+)/$', login_required(DeleteSubscribeuser.as_view(),login_url=loginurl), name='subscribedetail'),
	re_path(r'^subscribe_newsletter_add/$', views.subscribeuser, name='subscribe_newsletter_add'),

	re_path(r'^subscribelist/$', login_required(ListSubscribeUserAdmin.as_view(),login_url=loginurl), name='subscribelist'),
	re_path(r'^getuserlist_ajax', csrf_exempt(views.getuserlist_ajax), name='getuserlist_ajax'),

	re_path(r'^supportticket/$', login_required(AddSupportView.as_view()), name='supportticket'), 
	re_path(r'^tradeuser_supportticket/(?P<supportid>[-\w]+)/$', login_required(views.tradeusersupportreply_view), name='tradeuser_supportticket'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)