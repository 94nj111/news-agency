from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from news.models import Newspaper, Topic


class NewspaperSearchForm(forms.Form):
    topics = forms.ModelChoiceField(
        required=False,
        label="",
        queryset=Topic.objects.all(),
    )
