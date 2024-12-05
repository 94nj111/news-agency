from django.contrib.auth.mixins import LoginRequiredMixin


class RedactorRequiredMixin(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_redactor:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
    
    
class AdminRequiredMixin(LoginRequiredMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
