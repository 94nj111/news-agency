from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Redactor


@admin.register(Redactor)
class RedactorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_expirience",)
