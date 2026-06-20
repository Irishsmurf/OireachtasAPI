# coding: utf-8

import unittest
from unittest.mock import patch
import pytest

import oireachtas_api
from oireachtas_api.api.debates_api import DebatesApi


class TestDebatesApi(unittest.TestCase):
    """DebatesApi unit test stubs"""

    def setUp(self):
        self.api = oireachtas_api.api.debates_api.DebatesApi()

    def tearDown(self):
        pass

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_debates_mocked(self, mock_call_api):
        """Test case for debates (mocked)"""
        mock_response = {
            "results": [
                {
                    "debateRecord": {
                        "date": "2020-01-01",
                        "debateNo": 1,
                        "uri": "/ie/oireachtas/debate/2020-01-01/1"
                    }
                }
            ]
        }
        mock_call_api.return_value = mock_response

        response = self.api.debates(limit=1)
        mock_call_api.assert_called_once()
        self.assertEqual(response, mock_response)

    @pytest.mark.integration
    def test_debates_integration(self):
        """Test case for debates (integration)"""
        response = self.api.debates(limit=2)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.results)
        self.assertIsInstance(response.results, list)


if __name__ == '__main__':
    unittest.main()
