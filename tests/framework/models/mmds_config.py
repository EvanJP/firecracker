# coding: utf-8

"""
    Firecracker API

    RESTful public-facing API. The API is accessible through HTTP calls on specific URLs carrying JSON modeled data. The transport medium is a Unix Domain Socket.  # noqa: E501

    OpenAPI spec version: 0.23.0
    Contact: compute-capsule@amazon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MmdsConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ipv4_address': 'str'
    }

    attribute_map = {
        'ipv4_address': 'ipv4_address'
    }

    def __init__(self, ipv4_address='169.254.169.254'):  # noqa: E501
        """MmdsConfig - a model defined in Swagger"""  # noqa: E501
        self._ipv4_address = None
        self.discriminator = None
        if ipv4_address is not None:
            self.ipv4_address = ipv4_address

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this MmdsConfig.  # noqa: E501

        A valid IPv4 link-local address.  # noqa: E501

        :return: The ipv4_address of this MmdsConfig.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this MmdsConfig.

        A valid IPv4 link-local address.  # noqa: E501

        :param ipv4_address: The ipv4_address of this MmdsConfig.  # noqa: E501
        :type: str
        """

        self._ipv4_address = ipv4_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MmdsConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MmdsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
