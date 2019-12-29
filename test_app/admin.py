# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from test_app.models import Question, Choice

admin.site.register([Question, Choice])
