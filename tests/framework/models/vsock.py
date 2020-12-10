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

class Vsock(object):
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
        'guest_cid': 'int',
        'uds_path': 'str',
        'vsock_id': 'str'
    }

    attribute_map = {
        'guest_cid': 'guest_cid',
        'uds_path': 'uds_path',
        'vsock_id': 'vsock_id'
    }

    def __init__(self, guest_cid=None, uds_path=None, vsock_id=None):  # noqa: E501
        """Vsock - a model defined in Swagger"""  # noqa: E501
        self._guest_cid = None
        self._uds_path = None
        self._vsock_id = None
        self.discriminator = None
        self.guest_cid = guest_cid
        self.uds_path = uds_path
        self.vsock_id = vsock_id

    @property
    def guest_cid(self):
        """Gets the guest_cid of this Vsock.  # noqa: E501

        Guest Vsock CID  # noqa: E501

        :return: The guest_cid of this Vsock.  # noqa: E501
        :rtype: int
        """
        return self._guest_cid

    @guest_cid.setter
    def guest_cid(self, guest_cid):
        """Sets the guest_cid of this Vsock.

        Guest Vsock CID  # noqa: E501

        :param guest_cid: The guest_cid of this Vsock.  # noqa: E501
        :type: int
        """
        if guest_cid is None:
            raise ValueError("Invalid value for `guest_cid`, must not be `None`")  # noqa: E501

        self._guest_cid = guest_cid

    @property
    def uds_path(self):
        """Gets the uds_path of this Vsock.  # noqa: E501

        Path to UNIX domain socket, used to proxy vsock connections.  # noqa: E501

        :return: The uds_path of this Vsock.  # noqa: E501
        :rtype: str
        """
        return self._uds_path

    @uds_path.setter
    def uds_path(self, uds_path):
        """Sets the uds_path of this Vsock.

        Path to UNIX domain socket, used to proxy vsock connections.  # noqa: E501

        :param uds_path: The uds_path of this Vsock.  # noqa: E501
        :type: str
        """
        if uds_path is None:
            raise ValueError("Invalid value for `uds_path`, must not be `None`")  # noqa: E501

        self._uds_path = uds_path

    @property
    def vsock_id(self):
        """Gets the vsock_id of this Vsock.  # noqa: E501


        :return: The vsock_id of this Vsock.  # noqa: E501
        :rtype: str
        """
        return self._vsock_id

    @vsock_id.setter
    def vsock_id(self, vsock_id):
        """Sets the vsock_id of this Vsock.


        :param vsock_id: The vsock_id of this Vsock.  # noqa: E501
        :type: str
        """
        if vsock_id is None:
            raise ValueError("Invalid value for `vsock_id`, must not be `None`")  # noqa: E501

        self._vsock_id = vsock_id

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
        if issubclass(Vsock, dict):
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
        if not isinstance(other, Vsock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
