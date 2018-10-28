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
        request = self.factory.get('/')
        template_name = "included.html"
        context = include_by_ajax(context={'request': request}, template_name=template_name)
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], False)
        self.assertEquals(context['include_by_ajax_full_render'], False)
        self.assertEquals(context['template_name'], template_name)

    def test_access_by_ajax(self):
        request = self.factory.get('/', {
            'include_by_ajax_full_render': '1',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        template_name = "included.html"
        context = include_by_ajax(context={'request': request}, template_name=template_name)
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], False)
        self.assertEquals(context['include_by_ajax_full_render'], True)
        self.assertEquals(context['template_name'], template_name)

    def test_web_crawler_access(self):
        request = self.factory.get('/', HTTP_USER_AGENT='Googlebot')
        template_name = "included.html"
        context = include_by_ajax(context={'request': request}, template_name=template_name)
        self.assertEquals(context['include_by_ajax_no_placeholder_wrapping'], True)
        self.assertEquals(context['include_by_ajax_full_render'], True)
        self.assertEquals(context['template_name'], template_name)
