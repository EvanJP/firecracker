# coding: utf-8

"""
    Firecracker API

    RESTful public-facing API. The API is accessible through HTTP calls on specific URLs carrying JSON modeled data. The transport medium is a Unix Domain Socket.  # noqa: E501

    OpenAPI spec version: 0.23.0
    Contact: compute-capsule@amazon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.partial_drive import PartialDrive  # noqa: E501
from swagger_client.rest import ApiException


class TestPartialDrive(unittest.TestCase):
    """PartialDrive unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPartialDrive(self):
        """Test PartialDrive"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.partial_drive.PartialDrive()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
