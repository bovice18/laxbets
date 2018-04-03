# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Team, Game, Week, Pick, PlayerSubmission, Result

admin.site.register(Game)
admin.site.register(Pick)
admin.site.register(Result)
admin.site.register(Week)
admin.site.register(Team)
admin.site.register(PlayerSubmission)