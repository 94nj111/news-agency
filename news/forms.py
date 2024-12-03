from django import forms

from news.models import Newspaper, Topic


class NewspaperSearchForm(forms.Form):
    topics = forms.ModelChoiceField(
        required=False,
        label="",
        queryset=Topic.objects.all(),
    )
