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
from swagger_client.models.balloon_update import BalloonUpdate  # noqa: E501
from swagger_client.rest import ApiException


class TestBalloonUpdate(unittest.TestCase):
    """BalloonUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBalloonUpdate(self):
        """Test BalloonUpdate"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.balloon_update.BalloonUpdate()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
