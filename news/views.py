from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from news.models import Topic, Newspaper
from news.forms import NewspaperSearchForm


class NewspaperListView(generic.ListView):
    model = Newspaper
    queryset = Newspaper.objects.prefetch_related(
        "topics", "publishers"
    ).order_by("-published_date")
    paginate_by = 5

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


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = ["name"]
    success_url = reverse_lazy("news:topics")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    fields = ["name"]
    success_url = reverse_lazy("news:topics")
