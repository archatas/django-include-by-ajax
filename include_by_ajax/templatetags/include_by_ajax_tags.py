# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import template

register = template.Library()

@register.inclusion_tag('include_by_ajax/includes/placeholder.html', takes_context=True)
def include_by_ajax(context, template_name):
    request = context['request']
    if request.is_ajax() and request.GET.get('include_by_ajax_full_render'):
        context['include_by_ajax_full_render'] = template_name
    context['template_name'] = template_name
    return context
