from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from news.forms import NewspaperSearchForm
from news.models import Newspaper, Topic


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related(
        "topics", "publishers"
    ).order_by("-published_date")
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NewspaperListView, self).get_context_data(**kwargs)
        topics = self.request.GET.get("topics", "")
        context["search_form"] = NewspaperSearchForm(
            initial={"topics": topics}
        )
        return context

    def get_queryset(self):
        queryset = Newspaper.objects.prefetch_related("topics")
        topics = self.request.GET.get("topics")
        if topics:
            return queryset.filter(topics__in=topics)
        return queryset


class NewspaperDetailView(generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    fields = (
        "title",
        "content",
        "topics",
        "publishers",
        "photo",
    )
    success_url = reverse_lazy("news:index")


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = (
        "title",
        "content",
        "topics",
        "publishers",
        "photo",
    )
    success_url = reverse_lazy("news:index")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("news:index")


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 10


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = ("name",)
    success_url = reverse_lazy("news:topic-list")


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ("name",)
    success_url = reverse_lazy("news:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("news:topic-list")
