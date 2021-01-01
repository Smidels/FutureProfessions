from django import template
from profskills.models import ProfessionCategory, Skill, Profession

register = template.Library()


@register.simple_tag()
def get_profession_categories():
    return ProfessionCategory.objects.all()


@register.simple_tag()
def get_skills():
    return Skill.objects.all()


@register.simple_tag()
def get_professions():
    return Profession.objects.filter(is_published=True)
