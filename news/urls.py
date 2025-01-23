from django.urls import path

from news.views import (
    NewspaperCreateView,
    NewspaperDeleteView,
    NewspaperDetailView,
    NewspaperListView,
    NewspaperUpdateView,
    TopicCreateView,
    TopicDeleteView,
    TopicListView,
    TopicUpdateView,
)

urlpatterns = [
    path("", NewspaperListView.as_view(), name="index"),
    path("create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path("<int:pk>/", NewspaperDetailView.as_view(), name="newspaper-detail"),
    path(
        "<int:pk>/update/",
        NewspaperUpdateView.as_view(),
        name="newspaper-update",
    ),
    path(
        "<int:pk>/delete/",
        NewspaperDeleteView.as_view(),
        name="newspaper-delete",
    ),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update/",
        TopicUpdateView.as_view(),
        name="topic-update",
    ),
    path(
        "topics/<int:pk>/delete/",
        TopicDeleteView.as_view(),
        name="topic-delete",
    ),
]

app_name = "news"
