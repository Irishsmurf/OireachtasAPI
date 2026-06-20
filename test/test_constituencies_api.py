# coding: utf-8

import unittest
from unittest.mock import patch
import pytest

import oireachtas_api
from oireachtas_api.api.constituencies_api import ConstituenciesApi


class TestConstituenciesApi(unittest.TestCase):
    """ConstituenciesApi unit test stubs"""

    def setUp(self):
        self.api = oireachtas_api.api.constituencies_api.ConstituenciesApi()

    def tearDown(self):
        pass

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_constituencies_mocked(self, mock_call_api):
        """Test case for constituencies (mocked)"""
        mock_response = {
            "results": [
                {
                    "constituency": {
                        "constituencyCode": "carlow-kilkenny",
                        "showAs": "Carlow-Kilkenny",
                        "uri": "/ie/oireachtas/constituency/carlow-kilkenny"
                    }
                }
            ]
        }
        mock_call_api.return_value = mock_response

        response = self.api.constituencies(limit=1)
        mock_call_api.assert_called_once()
        self.assertEqual(response, mock_response)

    @pytest.mark.integration
    def test_constituencies_integration(self):
        """Test case for constituencies (integration)"""
        response = self.api.constituencies(limit=2)
        self.assertIsNotNone(response)
        self.assertIn('results', response)


if __name__ == '__main__':
    unittest.main()
