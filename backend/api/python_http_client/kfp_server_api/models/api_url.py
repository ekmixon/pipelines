# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class ApiUrl(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pipeline_url': 'str'
    }

    attribute_map = {
        'pipeline_url': 'pipeline_url'
    }

    def __init__(self, pipeline_url=None, local_vars_configuration=None):  # noqa: E501
        """ApiUrl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pipeline_url = None
        self.discriminator = None

        if pipeline_url is not None:
            self.pipeline_url = pipeline_url

    @property
    def pipeline_url(self):
        """Gets the pipeline_url of this ApiUrl.  # noqa: E501

        URL of the pipeline definition or the pipeline version definition.  # noqa: E501

        :return: The pipeline_url of this ApiUrl.  # noqa: E501
        :rtype: str
        """
        return self._pipeline_url

    @pipeline_url.setter
    def pipeline_url(self, pipeline_url):
        """Sets the pipeline_url of this ApiUrl.

        URL of the pipeline definition or the pipeline version definition.  # noqa: E501

        :param pipeline_url: The pipeline_url of this ApiUrl.  # noqa: E501
        :type pipeline_url: str
        """

        self._pipeline_url = pipeline_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        return (
            self.to_dict() == other.to_dict()
            if isinstance(other, ApiUrl)
            else False
        )

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return self.to_dict() != other.to_dict() if isinstance(other, ApiUrl) else True
