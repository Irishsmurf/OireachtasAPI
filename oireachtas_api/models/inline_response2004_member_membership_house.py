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


class InlineResponse2004MemberMembershipHouse(object):
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
        'house_code': 'str',
        'uri': 'str',
        'house_no': 'str',
        'show_as': 'str',
        'chamber_type': 'str'
    }

    attribute_map = {
        'house_code': 'houseCode',
        'uri': 'uri',
        'house_no': 'houseNo',
        'show_as': 'showAs',
        'chamber_type': 'chamberType'
    }

    def __init__(self, house_code=None, uri=None, house_no=None, show_as=None, chamber_type=None):  # noqa: E501
        """InlineResponse2004MemberMembershipHouse - a model defined in Swagger"""  # noqa: E501

        self._house_code = None
        self._uri = None
        self._house_no = None
        self._show_as = None
        self._chamber_type = None
        self.discriminator = None

        if house_code is not None:
            self.house_code = house_code
        if uri is not None:
            self.uri = uri
        if house_no is not None:
            self.house_no = house_no
        if show_as is not None:
            self.show_as = show_as
        if chamber_type is not None:
            self.chamber_type = chamber_type

    @property
    def house_code(self):
        """Gets the house_code of this InlineResponse2004MemberMembershipHouse.  # noqa: E501


        :return: The house_code of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :rtype: str
        """
        return self._house_code

    @house_code.setter
    def house_code(self, house_code):
        """Sets the house_code of this InlineResponse2004MemberMembershipHouse.


        :param house_code: The house_code of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :type: str
        """

        self._house_code = house_code

    @property
    def uri(self):
        """Gets the uri of this InlineResponse2004MemberMembershipHouse.  # noqa: E501


        :return: The uri of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this InlineResponse2004MemberMembershipHouse.


        :param uri: The uri of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def house_no(self):
        """Gets the house_no of this InlineResponse2004MemberMembershipHouse.  # noqa: E501


        :return: The house_no of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :rtype: str
        """
        return self._house_no

    @house_no.setter
    def house_no(self, house_no):
        """Sets the house_no of this InlineResponse2004MemberMembershipHouse.


        :param house_no: The house_no of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :type: str
        """

        self._house_no = house_no

    @property
    def show_as(self):
        """Gets the show_as of this InlineResponse2004MemberMembershipHouse.  # noqa: E501


        :return: The show_as of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :rtype: str
        """
        return self._show_as

    @show_as.setter
    def show_as(self, show_as):
        """Sets the show_as of this InlineResponse2004MemberMembershipHouse.


        :param show_as: The show_as of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :type: str
        """

        self._show_as = show_as

    @property
    def chamber_type(self):
        """Gets the chamber_type of this InlineResponse2004MemberMembershipHouse.  # noqa: E501


        :return: The chamber_type of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :rtype: str
        """
        return self._chamber_type

    @chamber_type.setter
    def chamber_type(self, chamber_type):
        """Sets the chamber_type of this InlineResponse2004MemberMembershipHouse.


        :param chamber_type: The chamber_type of this InlineResponse2004MemberMembershipHouse.  # noqa: E501
        :type: str
        """

        self._chamber_type = chamber_type

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
        if issubclass(InlineResponse2004MemberMembershipHouse, dict):
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
        if not isinstance(other, InlineResponse2004MemberMembershipHouse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other