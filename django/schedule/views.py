# -*- coding: utf-8 -*-

from django.http import Http404
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer
from schedule.decorator import validate_schedule_exists




class ScheduleList(generics.ListCreateAPIView):
    """ View for list all schedules or create a new schedule """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ScheduleSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @validate_schedule_exists
    def create(self, request, *args, **kargs):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Retrieve, update or delete a schedule instance """
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_object_or_404(self, pk):
        """ Get object or 404 """
        try:
            return Schedule.objects.get(pk=pk)
        except Schedule.DoesNotExist:
            raise Http404

    def retrieve(self, request, *args, **kwargs):
        """ Get a specific schedule """
        schedule = self.get_object_or_404(**kwargs)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data)

    @validate_schedule_exists
    def update(self, request, *args, **kwargs):
        """ Update a schedule """
        schedule = self.get_object_or_404(**kwargs)
        serializer = ScheduleSerializer(schedule, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """ Delete a schedule """
        schedule = self.get_object_or_404(**kwargs)
        schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
