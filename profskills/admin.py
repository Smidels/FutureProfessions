from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class ProfAdminForm(forms.ModelForm):
    # title = forms.CharField(widget=CKEditorUploadingWidget())

    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Profession
        fields = '__all__'


class ProfessionAdmin(admin.ModelAdmin):
    form = ProfAdminForm

    list_display = ('id', 'title', 'category', 'get_list_skills', 'is_published', 'created_at', 'created_by')
    list_display_links = ('id', 'title', 'category', 'get_list_skills')
    search_fields = ('title',)
    list_editable = ('is_published',)

    save_on_top = True

    def get_list_skills(self, profession):
        return [i for i in profession.skills.all()]


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_list_professions', 'get_list_info', 'created_at',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)

    def get_list_professions(self, skill):
        return [i for i in skill.profession_set.all()]

    def get_list_info(self, skill):
        return [i for i in skill.info.all()]


class SkillInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'category', 'get_list_sources', 'created_at')
    list_display_links = ('id', 'description', 'category', 'get_list_sources',)

    def get_list_sources(self, skill_info):
        return [i for i in skill_info.sources.all()]


class SkillInfoSourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'link', 'created_at')
    list_display_links = ('id', 'title', 'description', 'link', 'created_at')


class SkillInfoCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title',)


class ProfessionCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)


admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(SkillInfo, SkillInfoAdmin)
admin.site.register(SkillInfoSource, SkillInfoSourceAdmin)
admin.site.register(SkillInfoCategory, SkillInfoCategoryAdmin)
admin.site.register(ProfessionCategory, ProfessionCategoryAdmin)
