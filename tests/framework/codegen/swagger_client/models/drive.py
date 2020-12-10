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

class Drive(object):
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
        'drive_id': 'str',
        'is_read_only': 'bool',
        'is_root_device': 'bool',
        'partuuid': 'str',
        'path_on_host': 'str',
        'rate_limiter': 'RateLimiter'
    }

    attribute_map = {
        'drive_id': 'drive_id',
        'is_read_only': 'is_read_only',
        'is_root_device': 'is_root_device',
        'partuuid': 'partuuid',
        'path_on_host': 'path_on_host',
        'rate_limiter': 'rate_limiter'
    }

    def __init__(self, drive_id=None, is_read_only=None, is_root_device=None, partuuid=None, path_on_host=None, rate_limiter=None):  # noqa: E501
        """Drive - a model defined in Swagger"""  # noqa: E501
        self._drive_id = None
        self._is_read_only = None
        self._is_root_device = None
        self._partuuid = None
        self._path_on_host = None
        self._rate_limiter = None
        self.discriminator = None
        self.drive_id = drive_id
        self.is_read_only = is_read_only
        self.is_root_device = is_root_device
        if partuuid is not None:
            self.partuuid = partuuid
        self.path_on_host = path_on_host
        if rate_limiter is not None:
            self.rate_limiter = rate_limiter

    @property
    def drive_id(self):
        """Gets the drive_id of this Drive.  # noqa: E501


        :return: The drive_id of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._drive_id

    @drive_id.setter
    def drive_id(self, drive_id):
        """Sets the drive_id of this Drive.


        :param drive_id: The drive_id of this Drive.  # noqa: E501
        :type: str
        """
        if drive_id is None:
            raise ValueError("Invalid value for `drive_id`, must not be `None`")  # noqa: E501

        self._drive_id = drive_id

    @property
    def is_read_only(self):
        """Gets the is_read_only of this Drive.  # noqa: E501


        :return: The is_read_only of this Drive.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this Drive.


        :param is_read_only: The is_read_only of this Drive.  # noqa: E501
        :type: bool
        """
        if is_read_only is None:
            raise ValueError("Invalid value for `is_read_only`, must not be `None`")  # noqa: E501

        self._is_read_only = is_read_only

    @property
    def is_root_device(self):
        """Gets the is_root_device of this Drive.  # noqa: E501


        :return: The is_root_device of this Drive.  # noqa: E501
        :rtype: bool
        """
        return self._is_root_device

    @is_root_device.setter
    def is_root_device(self, is_root_device):
        """Sets the is_root_device of this Drive.


        :param is_root_device: The is_root_device of this Drive.  # noqa: E501
        :type: bool
        """
        if is_root_device is None:
            raise ValueError("Invalid value for `is_root_device`, must not be `None`")  # noqa: E501

        self._is_root_device = is_root_device

    @property
    def partuuid(self):
        """Gets the partuuid of this Drive.  # noqa: E501

        Represents the unique id of the boot partition of this device. It is optional and it will be taken into account only if the is_root_device field is true.  # noqa: E501

        :return: The partuuid of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._partuuid

    @partuuid.setter
    def partuuid(self, partuuid):
        """Sets the partuuid of this Drive.

        Represents the unique id of the boot partition of this device. It is optional and it will be taken into account only if the is_root_device field is true.  # noqa: E501

        :param partuuid: The partuuid of this Drive.  # noqa: E501
        :type: str
        """

        self._partuuid = partuuid

    @property
    def path_on_host(self):
        """Gets the path_on_host of this Drive.  # noqa: E501

        Host level path for the guest drive  # noqa: E501

        :return: The path_on_host of this Drive.  # noqa: E501
        :rtype: str
        """
        return self._path_on_host

    @path_on_host.setter
    def path_on_host(self, path_on_host):
        """Sets the path_on_host of this Drive.

        Host level path for the guest drive  # noqa: E501

        :param path_on_host: The path_on_host of this Drive.  # noqa: E501
        :type: str
        """
        if path_on_host is None:
            raise ValueError("Invalid value for `path_on_host`, must not be `None`")  # noqa: E501

        self._path_on_host = path_on_host

    @property
    def rate_limiter(self):
        """Gets the rate_limiter of this Drive.  # noqa: E501


        :return: The rate_limiter of this Drive.  # noqa: E501
        :rtype: RateLimiter
        """
        return self._rate_limiter

    @rate_limiter.setter
    def rate_limiter(self, rate_limiter):
        """Sets the rate_limiter of this Drive.


        :param rate_limiter: The rate_limiter of this Drive.  # noqa: E501
        :type: RateLimiter
        """

        self._rate_limiter = rate_limiter

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
        if issubclass(Drive, dict):
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
        if not isinstance(other, Drive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
