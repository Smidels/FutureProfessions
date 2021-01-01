from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
from django.contrib.auth import get_user

from .models import Profession, ProfessionCategory, Skill, SkillInfo, SkillInfoSource, SkillInfoCategory


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = ProfessionCategory
        title = forms.CharField(max_length=150)
        is_published = forms.BooleanField(widget=forms.CheckboxInput)

        fields = ['title', 'is_published']


class AddSourceForm(forms.ModelForm):
    class Meta:
        model = SkillInfoSource
        title = forms.CharField(max_length=150)
        description = forms.CharField(widget=forms.Textarea)
        link = forms.URLField(widget=forms.URLInput)

        fields = ['title', 'description', 'link']


class AddInfoForm(forms.ModelForm):
    class Meta:
        model = SkillInfo
        title = forms.CharField(max_length=150)
        description = forms.CharField(widget=forms.Textarea)
        category = forms.ModelChoiceField(queryset=SkillInfoCategory.objects.all(),
                                          widget=forms.Select)
        sources = forms.ModelMultipleChoiceField(queryset=SkillInfoSource.objects.all(),
                                                 widget=forms.SelectMultiple)

        fields = ['title', 'description', 'category', 'sources']


class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        title = forms.CharField(max_length=150)
        info = forms.ModelMultipleChoiceField(queryset=SkillInfo.objects.all(),
                                              widget=forms.SelectMultiple)

        fields = ['title', 'info']


class AddProfessionForm(forms.ModelForm):
    class Meta:
        model = Profession
        title = forms.CharField(max_length=150)
        category = forms.ModelChoiceField(queryset=ProfessionCategory.objects.all(),
                                          widget=forms.Select)
        description = forms.CharField(widget=forms.Textarea)
        skills = forms.ModelMultipleChoiceField(queryset=Skill.objects.all(),
                                                widget=forms.SelectMultiple)
        is_published = forms.BooleanField(widget=forms.CheckboxInput)
        fields = ['title', 'description', 'category', 'skills', 'is_published']

        widgets = {
            "description": CKEditorUploadingWidget()
        }
