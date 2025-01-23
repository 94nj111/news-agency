from django.urls import path

from accounts.views import (
    RedactorListView,
    RedactorRegisterView,
    RedactorUpdateView,
    RedactorDetailView,
    RedactorDeleteView,
    RedactorToggleView,
)

urlpatterns = [
    path("", RedactorListView.as_view(), name="redactor-list"),
    path("<int:pk>/", RedactorDetailView.as_view(), name="redactor-detail"),
    path(
        "<int:pk>/delete/",
        RedactorDeleteView.as_view(),
        name="redactor-delete",
    ),
    path(
        "<int:pk>/toggle/",
        RedactorToggleView.as_view(),
        name="redactor-toggle",
    ),
    path("signup/", RedactorRegisterView.as_view(), name="sign-up"),
    path(
        "<int:pk>/update/",
        RedactorUpdateView.as_view(),
        name="redactor-update",
    ),
]

app_name = "accounts"
