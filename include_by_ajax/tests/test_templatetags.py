# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test.client import RequestFactory

from include_by_ajax.templatetags.include_by_ajax_tags import include_by_ajax


class IncludeByAjaxTemplateTagTests(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factory = RequestFactory()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_first_access(self):
        # Given a request without any special query parameters and a template name
        request = self.factory.get('/')
        template_name = 'included.html'

        # When template tag {% include_by_ajax %} is called
        context = include_by_ajax(context={'request': request}, template_name=template_name)

        # Then we should get the template name saved in context variables
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], False)
        self.assertEquals(context['include_by_ajax_full_render'], False)
        self.assertEquals(context['template_name'], template_name)
        self.assertEquals(context['placeholder_template_name'], None)

    def test_first_access_with_loading_template(self):
        # Given a request without any special query parameters
        # and a template names for including and for temporary showing
        request = self.factory.get('/')
        template_name = 'included.html'
        placeholder_template_name = 'loading.html'

        # When template tag {% include_by_ajax %} is called
        context = include_by_ajax(
            context={'request': request},
            template_name=template_name,
            placeholder_template_name=placeholder_template_name,
        )

        # Then we should get the template names saved in context variables
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], False)
        self.assertEquals(context['include_by_ajax_full_render'], False)
        self.assertEquals(context['template_name'], template_name)
        self.assertEquals(context['placeholder_template_name'], placeholder_template_name)

    def test_access_by_ajax(self):
        # Given a request with include_by_ajax_full_render=1 query parameter and a template name
        request = self.factory.get('/', {
            'include_by_ajax_full_render': '1',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        template_name = 'included.html'

        # When template tag {% include_by_ajax %} is called
        context = include_by_ajax(context={'request': request}, template_name=template_name)

        # Then we should get the template name and include_by_ajax_full_render saved in context variables
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], False)
        self.assertEquals(context['include_by_ajax_full_render'], True)
        self.assertEquals(context['template_name'], template_name)
        self.assertEquals(context['placeholder_template_name'], None)

    def test_access_by_ajax_with_loading_template(self):
        # Given a request with include_by_ajax_full_render=1
        # and template names for including and for temporary showing
        request = self.factory.get('/', {
            'include_by_ajax_full_render': '1',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        template_name = 'included.html'
        placeholder_template_name = 'loading.html'

        # When template tag {% include_by_ajax %} is called
        context = include_by_ajax(
            context={'request': request},
            template_name=template_name,
            placeholder_template_name=placeholder_template_name,
        )

        # Then we should get the template names and include_by_ajax_full_render saved in context variables
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], False)
        self.assertEquals(context['include_by_ajax_full_render'], True)
        self.assertEquals(context['template_name'], template_name)
        self.assertEquals(context['placeholder_template_name'], placeholder_template_name)

    def test_web_crawler_access(self):
        # Given a request without special query parameters and a template name
        request = self.factory.get('/', HTTP_USER_AGENT='Googlebot')
        template_name = 'included.html'

        # When template tag {% include_by_ajax %} is called
        context = include_by_ajax(context={'request': request}, template_name=template_name)

        # Then we should get the template names, include_by_ajax_no_placeholder_wrapping,
        # and include_by_ajax_full_render saved in context variables
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], True)
        self.assertEquals(context['include_by_ajax_full_render'], True)
        self.assertEquals(context['template_name'], template_name)
        self.assertEquals(context['placeholder_template_name'], None)
