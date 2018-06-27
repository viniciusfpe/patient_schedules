# -*- coding: utf-8 -*-

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from schedule.models import Schedule    

def validate_schedule_exists(func):
    """ Decorator to validate if schedule date and time exist """
    def validate(self, request, **kwargs):
        date = request.data['date']
        start = request.data['start_time']
        end = request.data['end_time']

        if Schedule.is_range_conflict(date, start, end):
            return Response(
                'Horário não disponivel', status=status.HTTP_400_BAD_REQUEST)
        return func(self, request, **kwargs)
    return validate