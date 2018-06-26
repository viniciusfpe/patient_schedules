# -*- coding: utf-8 -*-

from django.contrib import admin

from schedule.models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """Schedule Admin."""

    pass

