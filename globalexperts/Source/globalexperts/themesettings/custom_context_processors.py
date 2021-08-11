from company.models import Company
from django.contrib.auth.models import User,Group
from django.db.models import Q
from trade_admin_auth.models import MenuPermissions
from trade_admin_auth.models import User_Kyc_Verification,User_Notification

def comp_profile(request):
    try:
        
        comp = Company.objects.get(id=1)

        host_url = "{0}://{1}".format(request.scheme, request.get_host())
        return {'comp_profile_name': comp.name,
                'comp_profile_id': comp.id,
                'company_fav' : comp.company_fav,
                'comp_company_logo' : comp.company_logo,
                'comp_video':comp.company_video,
                'host_url':host_url,
                'copy_right':comp.copy_right,
                'comp_email':comp.email,
                'comp_phonenumber':comp.phone1,
                'comp_gplus':comp.gplus,
                'comp_fb':comp.fb,
                'comp_twitter':comp.twitter,
                'comp_linkedin':comp.linkedin,
                'comp_instagram':comp.instagram,
                'comp_address':comp.address1,
                'comp_city':comp.city,
                'comp_state':comp.state,
                'comp_site':comp.website
            }
    except Company.DoesNotExist:
        return {
                'comp_profile_name': 'foo',
                'company_fav' : 'leaf',
                'comp_company_logo' : None,
                'comp_favicon' : None,
                'host_url':None,
                'copy_right':None,
                'comp_email':None,
                'comp_phonenumber':None,
                'comp_gplus':None,
                'comp_fb':None,
                'comp_twitter':None,
                'comp_linkedin':None,
                'comp_instagram':None
                }


def user_menupermissions(request):
    
    if (request.user.id):
        try:
            check_user = User.objects.get(Q(id = request.user.id) & (Q(admin_user_profile__role=0) | Q(admin_user_profile__role=1)))
            try:
                menu_permissions= MenuPermissions.objects.filter(user_permissions=request.user.id)
                menu_permissions_subadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=15))
                menu_permissions_cmsadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=6))
                menu_permissions_faqadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=4))
                menu_permissions_contactusadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=2))
                menu_permissions_emailadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=5))
                menu_permissions_manageuseradmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=1))
                menu_permissions_currencyadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=13))
                menu_permissions_tradeadmin= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=10))
                menu_permissions_referal= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=16))
                menu_permissions_ticket= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=7))
                menu_permissions_payment= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=11))
                menu_permissions_plan= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=17))
                menu_permissions_generation= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=18))
                menu_permissions_bank= MenuPermissions.objects.get(Q(user_permissions=request.user.id) & Q(access_modules=19))
                
                return {
                    'menu_permissions_context':menu_permissions,
                    'menu_permissions_subadmin':menu_permissions_subadmin.access_permissions,
                    'menu_permissions_cmsadmin':menu_permissions_cmsadmin.access_permissions,
                    'menu_permissions_faqadmin':menu_permissions_faqadmin.access_permissions,
                    'menu_permissions_contactusadmin':menu_permissions_contactusadmin.access_permissions,
                    'menu_permissions_emailadmin':menu_permissions_emailadmin.access_permissions,
                    'menu_permissions_manageuseradmin':menu_permissions_manageuseradmin.access_permissions,
                    'menu_permissions_currencyadmin':menu_permissions_currencyadmin.access_permissions,
                    'menu_permissions_tradeadmin':menu_permissions_tradeadmin.access_permissions,
                    'menu_permissions_referal':menu_permissions_referal.access_permissions,
                    'menu_permissions_ticket':menu_permissions_ticket.access_permissions,
                    'menu_permissions_payment':menu_permissions_payment.access_permissions,
                    'menu_permissions_plan':menu_permissions_plan.access_permissions,
                    'menu_permissions_generation':menu_permissions_generation.access_permissions,
                    'menu_permissions_bank':menu_permissions_bank.access_permissions,
                    
                }
            except MenuPermissions.DoesNotExist:
                return{}

        except User.DoesNotExist:
            return{}
    else:

        return{}


def trade_user(request):
    if (request.user.id):
        
        try:
            check_user_kyc_verification = User_Kyc_Verification.objects.get(user_kyc = request.user.id)
            get_kyc_verification_id = check_user_kyc_verification.id
            
        except User_Kyc_Verification.DoesNotExist:
            get_kyc_verification_id = ''
        
        try:
            check_notification = User_Notification.objects.get(user_notificatio = request.user.id)
            
            get_notification_id = check_notification.id
          
            
        except User_Notification.DoesNotExist:
            get_notification_id = ''
        
        return{
            'get_kyc_verification_id':get_kyc_verification_id,
            'get_notification_id':get_notification_id,
        }
    else:
        return{}