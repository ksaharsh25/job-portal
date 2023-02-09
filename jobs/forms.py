from dataclasses import fields
from django import forms
from django.contrib.admin.widgets import AutocompleteSelect
from .models import JobSeeker
from django.contrib import admin


class FakeRelation:
    def __init__(self, model):
        self.model = model


class CustomAutocompleteSelect (AutocompleteSelect):
    def __init__(self, model, admin_site, attrs=None, choices=(), using=None):
        rel = FakeRelation(model)
        super().__init__(rel, admin_site, attrs=attrs, choices=choices, using=using)

class JobseekerForm(forms.ModelForm):
    
    class Meta:
        model = JobSeeker
        fields = '__all__'