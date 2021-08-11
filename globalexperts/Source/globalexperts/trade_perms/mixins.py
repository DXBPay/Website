from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied


class OR_PermissionsRequiredMixin(AccessMixin):
    
    permission_required = None

    def get_permission_required(self):
       
        if self.permission_required is None:
            raise ImproperlyConfigured(
                '{0} is missing the permission_required attribute. Define {0}.permission_required, or override '
                '{0}.get_permission_required().'.format(self.__class__.__name__)
            )
        if isinstance(self.permission_required, str):
            perms = (self.permission_required, )
        else:
            perms = self.permission_required
        return perms

    def has_permission(self):
        
        perms = self.get_permission_required()
        
        if perms:
            for perm in perms:
                if self.request.user.has_perm(perm):
                    return True
        return False        
    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    
    
def shared_permission_access(user):
    permissions_list = ['trade_perms.Trade_Admin','trade_perms.Trade_Users' ]
    for permission in permissions_list:
        if user.has_perm(permission):
           return True
    raise  PermissionDenied
    return False 

def admin_permission_access(user, obj_id):
    if user.has_perm('trade_perms.Trade_Admin'):
           return True

    else:
        if user.id == obj_id:
            return True
            
    raise  PermissionDenied
    return False

