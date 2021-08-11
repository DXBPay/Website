from django.urls import include, path,re_path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
app_name = 'trade_master'

from . import views
from .views import UpdateCms_StaticContent,Liststaticcontent,DetailStaticcontent
from .views import UpdateCms_Content,Listcontent,Detailcontent
from .views import ListFaq,AddFaq,UpdateFaq,Detailfaq
from .views import Listcontactus,UpdateContactus,Detailcontactus
from .views import Listemailcontent,Updateemailcontenttemplate
from .views import AddTestimonial,ListTestimonial,UpdateTestimonial,DetailTestimonial
from .views import Blog_list,DetailBlog,UpdateBlogcontent,AddBlog,Marketingvideo_list
from .views import Updatevideo
loginurl='/LELPMDfDsmez0ksi/'

urlpatterns = [

	
	 re_path(r'^cms_page/(?P<pk>[-\w]+)/$', login_required(UpdateCms_StaticContent.as_view(),login_url=loginurl), name='cms_page'),
	 re_path(r'^cmspagelist/$', login_required(Liststaticcontent.as_view(),login_url=loginurl), name='cmspagelist'),
	 re_path(r'^cms_page_detail/(?P<pk>[-\w]+)/$', login_required(DetailStaticcontent.as_view(),login_url=loginurl), name='cms_page_detail'),

	 re_path(r'^cms_content/(?P<pk>[-\w]+)/$', login_required(UpdateCms_Content.as_view(),login_url=loginurl), name='cms_content'),
	 re_path(r'^cmspagecontentlist/$', login_required(Listcontent.as_view(),login_url=loginurl), name='cmspagecontentlist'),
	 re_path(r'^cms_page_contentdetail/(?P<pk>[-\w]+)/$', login_required(Detailcontent.as_view(),login_url=loginurl), name='cms_page_contentdetail'),

	 re_path(r'^updatetestimonial/(?P<pk>[-\w]+)/$', login_required(UpdateTestimonial.as_view(),login_url=loginurl), name='updatetestimonial'),
	 re_path(r'^testimoniallist/$', login_required(ListTestimonial.as_view(),login_url=loginurl), name='testimoniallist'),
	 re_path(r'^testimonialdetail/(?P<pk>[-\w]+)/$', login_required(DetailTestimonial.as_view(),login_url=loginurl), name='testimonialdetail'),
	 re_path(r'^addtestimonial/$', login_required(AddTestimonial.as_view(),login_url=loginurl), name='addtestimonial'),


	 re_path(r'^updatefaq/(?P<pk>[-\w]+)/$', login_required(UpdateFaq.as_view(),login_url=loginurl), name='updatefaq'),
	 re_path(r'^faqlist/$', login_required(ListFaq.as_view(),login_url=loginurl), name='faqlist'),
	 re_path(r'^addfaq/$', login_required(AddFaq.as_view(),login_url=loginurl), name='addfaq'),
	 re_path(r'^detail_faq/(?P<pk>[-\w]+)/$', login_required(Detailfaq.as_view(),login_url=loginurl), name='detail_faq'),

	 re_path(r'^contactus_update/(?P<pk>[-\w]+)/$', login_required(UpdateContactus.as_view(),login_url=loginurl), name='contactus_update'),
	 re_path(r'^contactlist/$', login_required(Listcontactus.as_view(),login_url=loginurl), name='contactlist'),
	 re_path(r'^contactusdetail/(?P<pk>[-\w]+)/$', login_required(Detailcontactus.as_view(),login_url=loginurl), name='contactusdetail'),

	 re_path(r'^updateemailcontent/(?P<pk>[-\w]+)/$', login_required(Updateemailcontenttemplate.as_view(),login_url=loginurl), name='updateemailcontent'),
	 re_path(r'^emailcontactlist/$', login_required(Listemailcontent.as_view(),login_url=loginurl), name='emailcontactlist'),

	re_path(r'^bloglist/$', login_required(Blog_list.as_view(),login_url=loginurl), name='bloglist'),
	re_path(r'^blog_detail/(?P<pk>[-\w]+)/$', login_required(DetailBlog.as_view(),login_url=loginurl), name='blog_detail'),
	re_path(r'^blog_page/(?P<pk>[-\w]+)/$', login_required(UpdateBlogcontent.as_view(),login_url=loginurl), name='blog_page'),
	re_path(r'^addblog/$', login_required(AddBlog.as_view(),login_url=loginurl), name='addblog'),


	re_path(r'^videolist/$', login_required(Marketingvideo_list.as_view(),login_url=loginurl), name='videolist'),
	re_path(r'^video_page/(?P<pk>[-\w]+)/$', login_required(Updatevideo.as_view(),login_url=loginurl), name='video_page'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)