from django.shortcuts import redirect
from django.http import HttpResponseForbidden


#for users to access bussines customer module
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        return wrapper_func
    return decorator

#for users to access admin/crm module
def staff_member_required(view_func):
    """
    Decorator to restrict access to staff members only.
    """
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated and is_staff
        if request.user.is_authenticated and request.user.is_staff:
            # User is staff, allow access to the view
            return view_func(request, *args, **kwargs)
        else:
            # User is not staff, deny access (return a forbidden response)
            return HttpResponseForbidden("You do not have permission to access this page.")
    
    return _wrapped_view