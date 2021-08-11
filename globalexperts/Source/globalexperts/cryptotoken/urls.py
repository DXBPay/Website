from django.urls import include, path,re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
app_name = 'cryptotoken'

from . import views
from .views import ListRoadMap,AddRoadMap,UpdateRoadMap,DetailRoadMap,ChangeTokenDetailView
from .views import ListCurrencyDetails,UpdateCurrencyDetail,DetailCurrencyDetail
from .views import AddTokenInformations,UpdateTokenInformations,ListTokenInformations,DetailToken
loginurl='/LELPMDfDsmez0ksi/'

urlpatterns = [

	re_path(r'^roadmapadd/$', login_required(AddRoadMap.as_view(),login_url=loginurl), name='roadmapadd'),
	re_path(r'^roadmaplist/$', login_required(ListRoadMap.as_view(),login_url=loginurl), name='roadmaplist'),
	re_path(r'^roademapdit/(?P<pk>[-\w]+)/$', login_required(UpdateRoadMap.as_view(),login_url=loginurl), name='roademapdit'),
	re_path(r'^roadmapdetail/(?P<pk>[-\w]+)/$', login_required(DetailRoadMap.as_view(),login_url=loginurl), name='roadmapdetail'),
	re_path(r'^tokensetting/(?P<pk>[-\w]+)/$', login_required(ChangeTokenDetailView.as_view(),login_url=loginurl), name='tokensetting'),
	re_path(r'^currencylist/$', login_required(ListCurrencyDetails.as_view(),login_url=loginurl), name='currencylist'),
	re_path(r'^currencyedit/(?P<pk>[-\w]+)/$', login_required(UpdateCurrencyDetail.as_view(),login_url=loginurl), name='currencyedit'),
	re_path(r'^currencydetail/(?P<pk>[-\w]+)/$', login_required(DetailCurrencyDetail.as_view(),login_url=loginurl), name='currencydetail'),

	re_path(r'^tokenadd/$', login_required(AddTokenInformations.as_view(),login_url=loginurl), name='tokenadd'),
	re_path(r'^tokenlist/$', login_required(ListTokenInformations.as_view(),login_url=loginurl), name='tokenlist'),
	re_path(r'^tokenedit/(?P<pk>[-\w]+)/$', login_required(UpdateTokenInformations.as_view(),login_url=loginurl), name='tokenedit'),
	re_path(r'^tokendetail/(?P<pk>[-\w]+)/$', login_required(DetailToken.as_view(),login_url=loginurl), name='tokendetail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)