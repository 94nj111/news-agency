from django import forms
from django.contrib.auth import get_user_model

from news.models import Newspaper, Topic


class NewspaperSearchForm(forms.Form):
    topics = forms.ModelChoiceField(
        required=False,
        label="",
        queryset=Topic.objects.all(),
    )
    publishers = forms.ModelChoiceField(
        required=False,
        label="",
        queryset=get_user_model().objects.filter(is_redactor=True)
    )
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"}),
    )
    
    
class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    topics = forms.ModelMultipleChoiceField(
        queryset=Topic.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    class Meta:
        model = Newspaper
        fields = (
            "title",
            "content",
            "photo",
        )
