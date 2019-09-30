
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class URLMapping(models.Model):
    """Stores mapping from original URL to shortened URL"""

    # Most web browsers support URLs up to 2048 characters or so
    original_url = models.CharField(
        max_length=2048, help_text="Original Url"
    )
    # Have to prepend this short_url_key with Host details
    short_url_key = models.CharField(
        max_length=20, null=True, help_text="Short URL"
    )

    def __str__(self):
        return "{self.original_url} -> {self.short_url_key}"

