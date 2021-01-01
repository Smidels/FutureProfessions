from django.urls import path
from .views import *

urlpatterns = [
    path('', ProfCategory.as_view(), name='home'),
    path('privacy-policy/', PrivacyPolicy.as_view(), name='privacy_policy'),
    path('category/<int:category_id>/', ProfessionByCategory.as_view(), name='category'),
    path('profession/<int:profession_id>/', ProfInfo.as_view(), name='profession_detail'),
    path('skill/<int:skill_id>/', SkillInfo.as_view(), name='skill_detail'),
    path('add_profession/', AddProfession.as_view(), name='add_profession'),
    path('add_skill/', AddSkill.as_view(), name='add_skill'),
    path('add_source/', AddSource.as_view(), name='add_source'),
    path('add_information/', AddInformation.as_view(), name='add_information'),
    path('add_category/', AddCategory.as_view(), name='add_category'),
    path('add_category/', AddCategory.as_view(), name='add_category'),

    path('studio/', Studio.as_view(), name='studio'),

    path('professions_library/', Professions.as_view(), name='professions'),
    path('skills_library/', Skills.as_view(), name='skills'),
]
