# -*- coding: utf-8 -*-

from django.db.models import Q
from rest_framework import status
from rest_framework.response import Response
from schedule.models import Schedule    

def validate_schedule_exists(func):
    """ Decorator to validate if schedule date and time exist """
    def validate(self, request, **kwargs):
        date = request.data['date']
        start_time = request.data['start_time']
        end_time = request.data['end_time']

        if Schedule.is_schedule_conflict(date, start_time, end_time):
            return Response(
                {'detail': 'Horário não disponivel'}, 
                status=status.HTTP_400_BAD_REQUEST)
        return func(self, request, **kwargs)
    return validate