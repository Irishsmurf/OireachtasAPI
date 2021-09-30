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

from swagger_client.configuration import Configuration


class InlineResponse2001QuestionBy(object):
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
        'show_as': 'object',
        'uri': 'object',
        'member_code': 'object'
    }

    attribute_map = {
        'show_as': 'showAs',
        'uri': 'uri',
        'member_code': 'memberCode'
    }

    def __init__(self, show_as=None, uri=None, member_code=None, _configuration=None):  # noqa: E501
        """InlineResponse2001QuestionBy - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._show_as = None
        self._uri = None
        self._member_code = None
        self.discriminator = None

        self.show_as = show_as
        self.uri = uri
        self.member_code = member_code

    @property
    def show_as(self):
        """Gets the show_as of this InlineResponse2001QuestionBy.  # noqa: E501


        :return: The show_as of this InlineResponse2001QuestionBy.  # noqa: E501
        :rtype: object
        """
        return self._show_as

    @show_as.setter
    def show_as(self, show_as):
        """Sets the show_as of this InlineResponse2001QuestionBy.


        :param show_as: The show_as of this InlineResponse2001QuestionBy.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and show_as is None:
            raise ValueError("Invalid value for `show_as`, must not be `None`")  # noqa: E501

        self._show_as = show_as

    @property
    def uri(self):
        """Gets the uri of this InlineResponse2001QuestionBy.  # noqa: E501


        :return: The uri of this InlineResponse2001QuestionBy.  # noqa: E501
        :rtype: object
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this InlineResponse2001QuestionBy.


        :param uri: The uri of this InlineResponse2001QuestionBy.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def member_code(self):
        """Gets the member_code of this InlineResponse2001QuestionBy.  # noqa: E501


        :return: The member_code of this InlineResponse2001QuestionBy.  # noqa: E501
        :rtype: object
        """
        return self._member_code

    @member_code.setter
    def member_code(self, member_code):
        """Sets the member_code of this InlineResponse2001QuestionBy.


        :param member_code: The member_code of this InlineResponse2001QuestionBy.  # noqa: E501
        :type: object
        """
        if self._configuration.client_side_validation and member_code is None:
            raise ValueError("Invalid value for `member_code`, must not be `None`")  # noqa: E501

        self._member_code = member_code

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
        if issubclass(InlineResponse2001QuestionBy, dict):
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
        if not isinstance(other, InlineResponse2001QuestionBy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001QuestionBy):
            return True

        return self.to_dict() != other.to_dict()
