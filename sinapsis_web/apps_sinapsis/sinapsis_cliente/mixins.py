from django.shortcuts import redirect

class OwnerSinapsisMixin(object):
    
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_sinapsis_owner:
            return super().dispatch(request,*args,**kwargs)
        
        return redirect("blog")
        
        
        
    # is_sinapsis_owner
    # is_sinapsis_manager
    # is_sinapsis_user 