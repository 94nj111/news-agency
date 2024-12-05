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


class RedactorPermissionMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        newspapers_ids = request.user.newspapers.values_list(
            "id",
        )
        if not request.user.is_superuser and not (
            (kwargs["pk"],) in newspapers_ids and request.user.is_redactor
        ):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and (kwargs["pk"],) == request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
