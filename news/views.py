from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from news.forms import NewspaperSearchForm, NewspaperForm
from news.models import Newspaper, Topic
from accounts.mixins import RedactorRequiredMixin, RedactorPermissionMixin


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related(
        "topics", "publishers"
    ).order_by("-published_date")
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        topics = self.request.GET.get("topics", "")
        publishers = self.request.GET.get("publishers", "")
        title = self.request.GET.get("title", "")
        context["search_form"] = NewspaperSearchForm(
            initial={
                "topics": topics,
                "publishers": publishers,
                "title": title,
            }
        )
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.prefetch_related("topics", "publishers")
        topics = self.request.GET.get("topics")
        publishers = self.request.GET.get("publishers")
        title = self.request.GET.get("title", "")
        if topics:
            queryset = queryset.filter(topics__in=topics)
        if publishers:
            queryset = queryset.filter(publishers__in=publishers)
        if title:
            queryset = queryset.filter(title__icontains=title)
        return queryset


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(RedactorRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("news:index")


class NewspaperUpdateView(RedactorPermissionMixin, generic.UpdateView):
    model = Newspaper
    form_class = NewspaperForm
    success_url = reverse_lazy("news:index")


class NewspaperDeleteView(RedactorPermissionMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:index")


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 10


class TopicCreateView(RedactorRequiredMixin, generic.CreateView):
    model = Topic
    fields = ("name",)
    success_url = reverse_lazy("news:topic-list")


class TopicUpdateView(RedactorRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ("name",)
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(RedactorRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news:topic-list")
