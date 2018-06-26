# Generated by Django 2.0.6 on 2018-06-25 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='data')),
                ('start_time', models.TimeField(verbose_name='horário de início')),
                ('end_time', models.TimeField(verbose_name='horário final')),
                ('patient', models.CharField(max_length=255, verbose_name='paciente')),
                ('procedure', models.TextField(verbose_name='procedimento')),
            ],
            options={
                'verbose_name_plural': 'Agendamentos',
                'verbose_name': 'Agendamento',
            },
        ),
    ]
