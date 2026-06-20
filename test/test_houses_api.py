# coding: utf-8

import unittest
from unittest.mock import patch
import pytest

import oireachtas_api
from oireachtas_api.api.houses_api import HousesApi


class TestHousesApi(unittest.TestCase):
    """HousesApi unit test stubs"""

    def setUp(self):
        self.api = oireachtas_api.api.houses_api.HousesApi()

    def tearDown(self):
        pass

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_houses_mocked(self, mock_call_api):
        """Test case for houses (mocked)"""
        mock_response = {
            "results": [
                {
                    "house": {
                        "houseCode": "dail",
                        "houseNo": "33",
                        "uri": "/ie/oireachtas/house/dail/33"
                    }
                }
            ]
        }
        mock_call_api.return_value = mock_response

        response = self.api.houses(limit=2)
        mock_call_api.assert_called_once()
        self.assertEqual(response, mock_response)

    @pytest.mark.integration
    def test_houses_integration(self):
        """Test case for houses (integration)"""
        response = self.api.houses(limit=2)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, dict)
        self.assertIn('results', response)


if __name__ == '__main__':
    unittest.main()
