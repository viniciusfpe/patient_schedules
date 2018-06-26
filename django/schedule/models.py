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

    class Meta:
        """ Class Meta """
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'