from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import RedactorCreationForm
from accounts.models import Redactor


class RedactorListView(generic.ListView):
    model = Redactor


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


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = (
        "email",
        "first_name",
        "last_name",
        "years_of_expirience",
        "photo",
    )
    success_url = reverse_lazy("accounts:redactor-list")
