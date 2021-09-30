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

from oireachtas_api.configuration import Configuration


class InlineResponse2003DivisionTallies(object):
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
        'nil_votes': 'Paths1divisionsgetresponses200schemapropertiesresultsitemsdefinitionsmemberTally',
        'ta_votes': 'Paths1divisionsgetresponses200schemapropertiesresultsitemsdefinitionsmemberTally',
        'staon_votes': 'object'
    }

    attribute_map = {
        'nil_votes': 'nilVotes',
        'ta_votes': 'taVotes',
        'staon_votes': 'staonVotes'
    }

    def __init__(self, nil_votes=None, ta_votes=None, staon_votes=None, _configuration=None):  # noqa: E501
        """InlineResponse2003DivisionTallies - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._nil_votes = None
        self._ta_votes = None
        self._staon_votes = None
        self.discriminator = None

        self.nil_votes = nil_votes
        self.ta_votes = ta_votes
        if staon_votes is not None:
            self.staon_votes = staon_votes

    @property
    def nil_votes(self):
        """Gets the nil_votes of this InlineResponse2003DivisionTallies.  # noqa: E501


        :return: The nil_votes of this InlineResponse2003DivisionTallies.  # noqa: E501
        :rtype: Paths1divisionsgetresponses200schemapropertiesresultsitemsdefinitionsmemberTally
        """
        return self._nil_votes

    @nil_votes.setter
    def nil_votes(self, nil_votes):
        """Sets the nil_votes of this InlineResponse2003DivisionTallies.


        :param nil_votes: The nil_votes of this InlineResponse2003DivisionTallies.  # noqa: E501
        :type: Paths1divisionsgetresponses200schemapropertiesresultsitemsdefinitionsmemberTally
        """
        if self._configuration.client_side_validation and nil_votes is None:
            raise ValueError("Invalid value for `nil_votes`, must not be `None`")  # noqa: E501

        self._nil_votes = nil_votes

    @property
    def ta_votes(self):
        """Gets the ta_votes of this InlineResponse2003DivisionTallies.  # noqa: E501


        :return: The ta_votes of this InlineResponse2003DivisionTallies.  # noqa: E501
        :rtype: Paths1divisionsgetresponses200schemapropertiesresultsitemsdefinitionsmemberTally
        """
        return self._ta_votes

    @ta_votes.setter
    def ta_votes(self, ta_votes):
        """Sets the ta_votes of this InlineResponse2003DivisionTallies.


        :param ta_votes: The ta_votes of this InlineResponse2003DivisionTallies.  # noqa: E501
        :type: Paths1divisionsgetresponses200schemapropertiesresultsitemsdefinitionsmemberTally
        """
        if self._configuration.client_side_validation and ta_votes is None:
            raise ValueError("Invalid value for `ta_votes`, must not be `None`")  # noqa: E501

        self._ta_votes = ta_votes

    @property
    def staon_votes(self):
        """Gets the staon_votes of this InlineResponse2003DivisionTallies.  # noqa: E501


        :return: The staon_votes of this InlineResponse2003DivisionTallies.  # noqa: E501
        :rtype: object
        """
        return self._staon_votes

    @staon_votes.setter
    def staon_votes(self, staon_votes):
        """Sets the staon_votes of this InlineResponse2003DivisionTallies.


        :param staon_votes: The staon_votes of this InlineResponse2003DivisionTallies.  # noqa: E501
        :type: object
        """

        self._staon_votes = staon_votes

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
        if issubclass(InlineResponse2003DivisionTallies, dict):
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
        if not isinstance(other, InlineResponse2003DivisionTallies):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2003DivisionTallies):
            return True

        return self.to_dict() != other.to_dict()
