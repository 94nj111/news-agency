from django.urls import path

from accounts.views import (
    RedactorListView,
    RedactorRegisterView,
    RedactorUpdateView,
)

urlpatterns = [
    path("", RedactorListView.as_view(), name="redactor-list"),
    path("signup/", RedactorRegisterView.as_view(), name="sign-up"),
    path("<int:pk>/update", RedactorUpdateView.as_view(), name="redactor-update"),
    
]

app_name = "accounts"
