# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import re

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class IncludeByAjaxConfig(AppConfig):
    name = "include_by_ajax"
    verbose_name = _("Include by Ajax")

    WEB_CRAWLERS_WITHOUT_JS = getattr(
        settings,
        "INCLUDE_BY_AJAX_WEB_CRAWLERS",
        (
            "Bingbot",  # Bing bot
            "Slurp",  # Yahoo! bot
            "DuckDuckBot",  # Duck Duck Go bot
            "Baiduspider",  # Baidu bot
            "YandexBot",  # Yandex bot
            "Sogou",  # Sogou bot
            "Exabot",  # Exalead bot
            "ia_archiver",  # Alexa bot
        ),
    )
    web_crawler_pattern = re.compile(
        "|".join(sorted(WEB_CRAWLERS_WITHOUT_JS, reverse=True)), flags=re.IGNORECASE
    )

    def ready(self):
        pass
