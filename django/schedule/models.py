# -*- coding: utf-8 -*-

from django.db import models


class Schedule(models.Model):
    """ Schedules """
    date = models.DateField('data')
    start_time = models.TimeField('horário de início')
    end_time = models.TimeField('horário final')
    patient = models.CharField('paciente', max_length=255)
    procedure = models.TextField('procedimento')

    def __str__(self):
        return "Paciente: {} Data: {} {} até {}.".format(
            self.patient,
            self.date,
            self.start_time,
            self.end_time)
    
    @classmethod
    def is_range_conflict(cls, date, start, end):
        """ Verify if schedule is conflict with other schedule """
        range_start = cls.objects.filter(
            date=date, start_time__lt=end, start_time__gt=start).exists()

        range_end = cls.objects.filter(
            date=date, end_time__lt=end, end_time__gt=start).exists()

        range_times = cls.objects.filter(
            date=date, start_time__lte=start, end_time__gte=end).exists()

        return range_start or range_end or range_times

    class Meta:
        """ Class Meta """
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'