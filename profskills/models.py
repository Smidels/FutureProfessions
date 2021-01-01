from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
# from django.contrib.auth.models import CustomUser
from jobservice import settings
from users.models import CustomUser


class SkillInfoCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Info Category'
        verbose_name_plural = 'Info Categories'
        ordering = ['-created_at']


class SkillInfoSource(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    link = models.URLField(max_length=200, verbose_name='Link')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Info Source'
        verbose_name_plural = 'Info Sources'
        ordering = ['-created_at']


class SkillInfo(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField(verbose_name='Description', blank=True)
    category = models.ForeignKey(SkillInfoCategory, on_delete=models.PROTECT)
    sources = models.ManyToManyField(SkillInfoSource, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill Info'
        verbose_name_plural = 'Skill Info'
        ordering = ['-created_at']


class Skill(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    info = models.ManyToManyField(SkillInfo, blank=True, verbose_name='Info')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['-created_at']


class ProfessionCategory(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    is_published = models.BooleanField(default=True, verbose_name='Published')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Profession Category'
        verbose_name_plural = 'Profession Categories'
        ordering = ['title']


class Profession(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Title')
    category = models.ForeignKey(ProfessionCategory, on_delete=models.PROTECT)
    description = models.TextField(verbose_name='Description',
                                   blank=True)  # треба буде добавити модель, аналогічно скілам
    skills = models.ManyToManyField(Skill, blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True, )

    def get_absolute_url(self):
        return reverse_lazy('profession_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Profession'
        verbose_name_plural = 'Professions'
        ordering = ['-created_at']
