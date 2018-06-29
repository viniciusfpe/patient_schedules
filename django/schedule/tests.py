# -*- coding: utf-8 -*-

import json

from django.test import TestCase


class TestScheduleList(TestCase):
    """ Test get schedule list """

    fixtures = ['schedule.json']

    def setUp(self):
        pass

    def test_get_schedules(self):
        response = self.client.get(
            '/api/schedules/', content_type='application/json'
        )

        self.assertEqual(200, response.status_code)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(isinstance(data, list))
        self.assertTrue(isinstance(data[0], dict))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['date'], '2018-06-30')
        self.assertEqual(data[0]['start_time'], '15:00:00')
        self.assertEqual(data[0]['end_time'], '16:00:00')
        self.assertEqual(data[0]['patient'], 'Vinicius Peixoto')
        self.assertEqual(data[0]['procedure'], 'Primeira consulta')
        
