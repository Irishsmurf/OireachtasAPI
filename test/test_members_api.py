# coding: utf-8

import unittest
from unittest.mock import patch
import pytest

import oireachtas_api
from oireachtas_api.api.members_api import MembersApi


class TestMembersApi(unittest.TestCase):
    """MembersApi unit test stubs"""

    def setUp(self):
        self.api = oireachtas_api.api.members_api.MembersApi()

    def tearDown(self):
        pass

    @patch('oireachtas_api.api_client.ApiClient.call_api')
    def test_members_mocked(self, mock_call_api):
        """Test case for members (mocked)"""
        mock_response = {
            "results": [
                {
                    "member": {
                        "fullName": "Leo Varadkar",
                        "memberCode": "LeoVaradkar",
                        "uri": "/ie/oireachtas/member/leo-varadkar"
                    }
                }
            ]
        }
        mock_call_api.return_value = mock_response

        response = self.api.members(limit=1)
        mock_call_api.assert_called_once()
        self.assertEqual(response, mock_response)

    @pytest.mark.integration
    def test_members_integration(self):
        """Test case for members (integration)"""
        response = self.api.members(limit=2)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.results)
        self.assertIsInstance(response.results, list)


if __name__ == '__main__':
    unittest.main()
