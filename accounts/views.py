from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect

from accounts.forms import RedactorCreationForm, RedactorSearchForm
from accounts.models import Redactor
from accounts.mixins import AdminRequiredMixin, UserPermissionMixin


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(
            initial={
                "username": username,
            }
        )
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        username = self.request.GET.get("username")
        if username:
            queryset = queryset.filter(username__icontains=username)
        return queryset


class RedactorDetailView(generic.DetailView):
    model = Redactor


class RedactorDeleteView(AdminRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("accounts:redactor-list")


class RedactorRegisterView(generic.View):

    def post(self, request):
        form = RedactorCreationForm(request.POST or None)

        if request.method == "POST":
            if form.is_valid():
                user = form.save()
                user.save()
                login(request, user)

                return redirect("news:index")

        return render(request, "registration/register.html", {"form": form})

    def get(self, request):
        form = RedactorCreationForm()
        return render(request, "registration/register.html", {"form": form})


class RedactorUpdateView(UserPermissionMixin, generic.UpdateView):
    model = Redactor
    fields = (
        "email",
        "first_name",
        "last_name",
        "years_of_expirience",
        "photo",
    )
    success_url = reverse_lazy("accounts:redactor-list")


class RedactorToggleView(AdminRequiredMixin, generic.View):

    def get(self, request, pk):
        redactor = Redactor.objects.get(id=pk)
        if redactor.is_redactor:
            redactor.is_redactor = False
        else:
            redactor.is_redactor = True
        redactor.save()
        return HttpResponseRedirect(reverse_lazy("accounts:redactor-detail", args=[pk]))
