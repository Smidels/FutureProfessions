from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import *
from .models import Profession, Skill, ProfessionCategory, SkillInfoSource, SkillInfo


class Studio(LoginRequiredMixin, TemplateView):
    template_name = 'profskills/studio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['professions'] = Profession.objects.order_by('-created_at')[:]
        context['skills'] = Skill.objects.all().order_by('-created_at')[:]
        # context['skill_info'] = SkillInfo.objects.all().order_dy('created_at').desc()
        # context['SkillInfoSource'] = SkillInfoSource.objects.all().order_dy('created_at').desc()
        return context


class AddCategory(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AddCategoryForm
    template_name = 'profskills/add_category.html'
    success_url = reverse_lazy('add_category')
    login_url = '/admin/'
    success_message = 'Category was created successfully'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AddSource(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AddSourceForm
    template_name = 'profskills/add_source.html'
    success_url = reverse_lazy('add_source')
    login_url = '/admin/'
    success_message = 'Source was created successfully'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AddInformation(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AddInfoForm
    template_name = 'profskills/add_information.html'
    success_url = reverse_lazy('add_information')
    login_url = '/admin/'
    success_message = 'Info was created successfully'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AddSkill(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AddSkillForm
    template_name = 'profskills/add_skill.html'
    success_url = reverse_lazy('add_skill')
    login_url = '/admin/'
    success_message = 'Skill was created successfully'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AddProfession(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    form_class = AddProfessionForm
    template_name = 'profskills/add_profession.html'
    success_url = reverse_lazy('add_profession')  # задаємо куди буде кидати після відправки форми
    # по дефолту бере get_absolute_url з моделі
    login_url = '/admin/'  # кидає на авторизацію
    # reise_exception = True # видає 403
    success_message = 'Profession was created successfully'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class SkillInfo(DetailView):
    model = Skill
    # context_object_name = 'profession'
    template_name = 'profskills/skill_details.html'
    pk_url_kwarg = 'skill_id'


class ProfCategory(ListView):
    model = ProfessionCategory
    template_name = 'profskills/index.html'
    context_object_name = 'prof_categories'

    def get_queryset(self):
        return ProfessionCategory.objects.filter(is_published=True)


class Skills(ListView):
    model = Skill
    template_name = 'profskills/skills_list.html'
    context_object_name = 'skills'


# def get_queryset(self):
# 	return Skills.objects.filter(is_published=True)


class Professions(ListView):
    model = Profession
    template_name = 'profskills/professions_list.html'
    context_object_name = 'professions'

    def get_queryset(self):
        return Profession.objects.filter(is_published=True)


class ProfessionByCategory(ListView):
    model = Profession
    template_name = 'profskills/profession_by_category.html'
    context_object_name = 'professions'
    allow_empty = False

    def get_queryset(self):
        return Profession.objects.filter(
            category_id=self.kwargs['category_id'],
            is_published=True,
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = ProfessionCategory.objects.get(pk=self.kwargs['category_id'])
        return context


class ProfInfo(DetailView):
    model = Profession
    # context_object_name = 'profession'
    template_name = 'profskills/profession_details.html'
    pk_url_kwarg = 'profession_id'  # дозволяє отримати pk з id, бо DetailView вимагає pk


# # def get_queryset(self):
# # 	return Profession.objects.filter(
# # 		id=self.kwargs['id'],
# # 		is_published=True,
# # 		)


# 	def get_context_data(self, *, object_list=None, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 	# context['category'] = Profession.objects.get(pk=self.kwargs['category_id'])
# 	# context['title'] = Profession.objects.get(pk=self.kwargs['title'])
# 	return context


class PrivacyPolicy(TemplateView):
    template_name = 'profskills/privacy_policy.html'
