# -*- coding: utf-8 -*-

import json

from django.test import TestCase
from rest_framework import status


class TestScheduleList(TestCase):
    """ Test get schedule list """

    fixtures = ['schedule.json']

    def setUp(self):
        pass

    def assert_response(self, data):
        self.assertEqual(data['id'], 1)
        self.assertEqual(data['date'], '2018-06-30')
        self.assertEqual(data['start_time'], '15:00:00')
        self.assertEqual(data['end_time'], '16:00:00')
        self.assertEqual(data['patient'], 'Vinicius Peixoto')
        self.assertEqual(data['procedure'], 'Primeira consulta')

    def test_get_schedules(self):
        
        response = self.client.get(
            '/api/schedules/', content_type='application/json'
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))
        self.assertEqual(len(data), 1)
        self.assert_response(data[0])
    
    def test_get_schedule_by_id(self):
        
        response = self.client.get(
            '/api/schedule/1/', content_type='application/json'
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, dict))
        self.assert_response(data)

    def test_update_schedule_by_id(self):

        payload = {
            'date': '2018-06-30',
            'start_time': '17:00',
            'end_time': '18:00',
            'patient': 'Vinicius Peixoto',
            'procedure': 'Primeira consulta'
        }

        response = self.client.put(
            '/api/schedule/1/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['start_time'], '17:00:00')
        self.assertEqual(data['end_time'], '18:00:00')

    def test_delete_schedule_by_id(self):
        
        response = self.client.delete(
            '/api/schedule/1/', content_type='application/json'
        )

        self.assertEqual(
            status.HTTP_204_NO_CONTENT, response.status_code)

        test_delete = self.client.get(
            '/api/schedule/1/', content_type='application/json'
        )

        self.assertEqual(
            status.HTTP_404_NOT_FOUND, test_delete.status_code)
    
    def test_post_schedule(self):
        
        payload = {
            'date': '2018-06-30',
            'start_time': '12:00',
            'end_time': '13:00',
            'patient': 'João da Silva',
            'procedure': 'Realizar exames de rotina'
        }

        response = self.client.post(
            '/api/schedules/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            status.HTTP_201_CREATED, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['id'], 2)
        self.assertEqual(data['date'], '2018-06-30')
        self.assertEqual(data['start_time'], '12:00:00')
        self.assertEqual(data['end_time'], '13:00:00')
        self.assertEqual(data['patient'], 'João da Silva')
        self.assertEqual(data['procedure'], 'Realizar exames de rotina')
    
    def test_post_schedule_schedule_exists(self):
        
        payload = {
            'date': '2018-06-30',
            'start_time': '14:30',
            'end_time': '15:30',
            'patient': 'Folgado carvalho',
            'procedure': 'Quer marcar um horário urgente'
        }

        response = self.client.post(
            '/api/schedules/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            status.HTTP_400_BAD_REQUEST, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['detail'], 'Horário não disponivel')

    def test_put_schedule_schedule_exists(self):
        
        payload = {
            'date': '2018-06-30',
            'start_time': '14:30',
            'end_time': '16:30',
            'patient': 'Folgado carvalho',
            'procedure': 'Quer marcar um horário urgente'
        }

        response = self.client.put(
            '/api/schedule/1/',
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(
            status.HTTP_400_BAD_REQUEST, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, dict))
        self.assertEqual(data['detail'], 'Horário não disponivel')
