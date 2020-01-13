# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from TimeSeriesIoT.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_allrecords_get(self):
        """Test case for allrecords_get

        Retourne toutes les captures des capteurs
        """
        response = self.client.open(
            '/v1/allrecords',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_last_sensor_id_get(self):
        """Test case for last_sensor_id_get

        Calculer la dernière valeur
        """
        response = self.client.open(
            '/v1/last/{sensorId}'.format(sensor_id='sensor_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mean_sensor_id_get(self):
        """Test case for mean_sensor_id_get

        Calculer la moyenne d'un capteur entre deux dates
        """
        query_string = [('start_date', 56),
                        ('end_date', 56)]
        response = self.client.open(
            '/v1/mean/{sensorId}'.format(sensor_id='sensor_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_min_sensor_id_get(self):
        """Test case for min_sensor_id_get

        Calculer la valeur minimale d'un capteur entre deux dates
        """
        query_string = [('start_date', 56),
                        ('end_date', 56)]
        response = self.client.open(
            '/v1/min/{sensorId}'.format(sensor_id='sensor_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
