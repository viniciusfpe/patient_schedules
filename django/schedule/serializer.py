# -*- coding: utf-8 -*-

from rest_framework import serializers
from schedule.models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    """ API for create, update, delete and list schedules """

    class Meta:
        """ Class Meta """
        model = Schedule
        fields = '__all__'