# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import apps
from django import template

register = template.Library()


@register.inclusion_tag('include_by_ajax/includes/placeholder.html', takes_context=True)
def include_by_ajax(context, template_name):
    # get the app configuration
    app_config = apps.get_app_config('include_by_ajax')
    # get User-Agent
    request = context['request']
    user_agent = request.META.get('HTTP_USER_AGENT') or ''
    # check if the current request is coming from a web crawler
    is_web_crawler = bool(app_config.web_crawler_pattern.search(user_agent))
    # in case of web crawler or an Ajax call we'll do full render
    context['include_by_ajax_full_render'] = bool(
        is_web_crawler or
        request.is_ajax() and request.GET.get('include_by_ajax_full_render')
    )
    # in case of web crawler, the placeholder shouldn't be wrapped with a <section>
    context['include_by_ajax_no_placeholder_wrapping'] = is_web_crawler
    # pass down the template path
    context['template_name'] = template_name
    return context
