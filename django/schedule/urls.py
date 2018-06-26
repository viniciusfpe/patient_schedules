# -*- coding: utf-8 -*-

from django.urls import path
from schedule.views import ScheduleList, ScheduleDetail

urlpatterns = [
    path('schedules/', ScheduleList.as_view(), name='schedule_list'),
    path('schedule/<int:pk>/', ScheduleDetail.as_view(), name='schedule_details'),
]