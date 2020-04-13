# coding: utf-8

"""
    Houses of the Oireachtas Open Data APIs

    The Houses of the Oireachtas is providing these APIs to allow our datasets to be retrieved and reused as widely as possible. They are intended to be used in conjunction with https://data.oireachtas.ie, from where our datasets can be accessed directly. By using the APIs, users can make metadata queries to identify the specific data they require. New data are available through the API as soon as they are published.  Currently, https://data.oireachtas.ie contains data in XML format from the Official Report of the Houses of the Oireachtas (the \"debates\") and replies to Parliamentary Questions in XML files complying with the [Akoma Ntoso](http://akomantoso.org) schema, as well data in PDF format for Bills, Acts and other documents published by the Houses of the Oireachtas.  Files can be retrieved from https://data.oireachtas.ie by adding the URI fragment contained in the \"formats\" fields of the JSON documents returned by these APIs. At the moment only PDF and XML files are available directly from https://data.oireachtas.ie, but this will become the endpoint for direct access of all \"uri\" fields in the data queried through https://api.oireachtas.ie. We will also be making bulk downloads available through https://data.oireachtas.ie.  Please note the APIs are a work in progress. We are working on expanding the range of datasets we publish, and we are interested in hearing about how to make these APIs more useful and wide ranging. For these reasons, we welcome any feedback, suggestions and user stories to open.data@oireachtas.ie  Data published through these APIs are made available under the [Oireachtas (Open Data) PSI Licence](https://beta.oireachtas.ie/en/open-data/license/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: open.data@oireachtas.ie
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200Head(object):
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
        'counts': 'object',
        'date_range': 'InlineResponse200HeadDateRange',
        'lang': 'str'
    }

    attribute_map = {
        'counts': 'counts',
        'date_range': 'dateRange',
        'lang': 'lang'
    }

    def __init__(self, counts=None, date_range=None, lang=None):  # noqa: E501
        """InlineResponse200Head - a model defined in Swagger"""  # noqa: E501

        self._counts = None
        self._date_range = None
        self._lang = None
        self.discriminator = None

        if counts is not None:
            self.counts = counts
        if date_range is not None:
            self.date_range = date_range
        if lang is not None:
            self.lang = lang

    @property
    def counts(self):
        """Gets the counts of this InlineResponse200Head.  # noqa: E501


        :return: The counts of this InlineResponse200Head.  # noqa: E501
        :rtype: object
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this InlineResponse200Head.


        :param counts: The counts of this InlineResponse200Head.  # noqa: E501
        :type: object
        """

        self._counts = counts

    @property
    def date_range(self):
        """Gets the date_range of this InlineResponse200Head.  # noqa: E501


        :return: The date_range of this InlineResponse200Head.  # noqa: E501
        :rtype: InlineResponse200HeadDateRange
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """Sets the date_range of this InlineResponse200Head.


        :param date_range: The date_range of this InlineResponse200Head.  # noqa: E501
        :type: InlineResponse200HeadDateRange
        """

        self._date_range = date_range

    @property
    def lang(self):
        """Gets the lang of this InlineResponse200Head.  # noqa: E501


        :return: The lang of this InlineResponse200Head.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this InlineResponse200Head.


        :param lang: The lang of this InlineResponse200Head.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "ga", "mul"]  # noqa: E501
        if lang not in allowed_values:
            raise ValueError(
                "Invalid value for `lang` ({0}), must be one of {1}"  # noqa: E501
                .format(lang, allowed_values)
            )

        self._lang = lang

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
        if issubclass(InlineResponse200Head, dict):
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
        if not isinstance(other, InlineResponse200Head):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
