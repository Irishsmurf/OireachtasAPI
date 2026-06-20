# coding: utf-8

import unittest
from unittest.mock import patch, MagicMock
import pytest

import oireachtas_api


class TestClient(unittest.TestCase):
    """Unit tests for the simplified Oireachtas Client class."""

    def test_client_initialization_defaults(self):
        """Test client initialization with default configuration settings."""
        client = oireachtas_api.Client()
        self.assertEqual(client.configuration.host, "https://api.oireachtas.ie/v1")
        self.assertTrue(client.configuration.verify_ssl)
        self.assertFalse(client.configuration.debug)

    def test_client_initialization_custom(self):
        """Test client initialization with custom configurations."""
        client = oireachtas_api.Client(
            host="https://custom.api.endpoint/v1",
            debug=True,
            verify_ssl=False,
            proxy="http://localhost:3128"
        )
        self.assertEqual(client.configuration.host, "https://custom.api.endpoint/v1")
        self.assertFalse(client.configuration.verify_ssl)
        self.assertTrue(client.configuration.debug)
        self.assertEqual(client.configuration.proxy, "http://localhost:3128")

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_constituencies_mocked(self, mock_call_api):
        """Test constituencies call converting model mock to dictionary."""
        # Using a Mock Swagger object that behaves like a swagger model with to_dict()
        mock_response = MagicMock()
        mock_response.to_dict.return_value = {
            "results": [
                {
                    "constituency": {
                        "constituencyCode": "carlow-kilkenny",
                        "showAs": "Carlow-Kilkenny"
                    }
                }
            ]
        }
        mock_call_api.return_value = mock_response

        client = oireachtas_api.Client()
        response = client.constituencies(limit=1)

        self.assertIsInstance(response, dict)
        self.assertEqual(response["results"][0]["constituency"]["constituencyCode"], "carlow-kilkenny")
        mock_call_api.assert_called_once()

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_members_mocked(self, mock_call_api):
        """Test members call converting model mock to dictionary."""
        mock_response = MagicMock()
        mock_response.to_dict.return_value = {
            "results": [
                {
                    "member": {
                        "fullName": "Michael D. Higgins",
                        "memberId": "123"
                    }
                }
            ]
        }
        mock_call_api.return_value = mock_response

        client = oireachtas_api.Client()
        response = client.members(limit=1, party_code="FF")

        self.assertIsInstance(response, dict)
        self.assertEqual(response["results"][0]["member"]["fullName"], "Michael D. Higgins")
        mock_call_api.assert_called_once()

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_api_exception_export(self, mock_call_api):
        """Test client raises oireachtas_api.ApiException on error."""
        from oireachtas_api.rest import ApiException
        mock_call_api.side_effect = ApiException(status=404, reason="Not Found")

        client = oireachtas_api.Client()
        with self.assertRaises(oireachtas_api.ApiException) as context:
            client.constituencies()

        self.assertEqual(context.exception.status, 404)

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_constituencies_async(self, mock_call_api):
        """Test constituencies call with async_req=True returns wrapped AsyncResult."""
        mock_response = MagicMock()
        mock_response.to_dict.return_value = {"results": []}

        class ApplyResult:
            def get(self, timeout=None):
                return mock_response

        mock_call_api.return_value = ApplyResult()

        client = oireachtas_api.Client()
        async_res = client.constituencies(limit=1, async_req=True)
        
        self.assertEqual(type(async_res).__name__, 'AsyncResult')
        
        response = async_res.get()
        self.assertIsInstance(response, dict)
        self.assertEqual(response, {"results": []})

    @pytest.mark.integration
    def test_client_integration(self):
        """Live integration tests for the simplified client."""
        client = oireachtas_api.Client()
        
        # 1. Test constituencies
        response = client.constituencies(limit=2)
        self.assertIsInstance(response, dict)
        self.assertIn("results", response)
        self.assertGreater(len(response["results"]), 0)

        # 2. Test houses
        houses_response = client.houses(limit=2)
        self.assertIsInstance(houses_response, dict)
        self.assertIn("results", houses_response)

        # 3. Test parties
        parties_response = client.parties(limit=2)
        self.assertIsInstance(parties_response, dict)
        self.assertIn("results", parties_response)


if __name__ == '__main__':
    unittest.main()
