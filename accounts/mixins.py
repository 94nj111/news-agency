from django.contrib.auth.mixins import AccessMixin


class RedactorRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_redactor:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class RedactorPermissionMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        newspapers_ids = request.user.newspapers.values_list(
            "id",
        )
        if not request.user.is_superuser and not (
            (kwargs["pk"],) in newspapers_ids and request.user.is_redactor
        ):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not (request.user.is_superuser or (kwargs["pk"]) == request.user.id):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
