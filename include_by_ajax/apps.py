# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class IncludeByAjaxConfig(AppConfig):
    name = 'include_by_ajax'
    verbose_name = _("Include by Ajax")

    def ready(self):
        pass
