from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login

from accounts.models import Redactor
from accounts.forms import RedactorCreationForm


class RedactorListView(generic.ListView):
    model = Redactor
    
    
class RedactorRegisterView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    template_name = "registration/register.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = (
        "email",
        "first_name",
        "last_name",
        "years_of_expirience",
        "photo",
    )
