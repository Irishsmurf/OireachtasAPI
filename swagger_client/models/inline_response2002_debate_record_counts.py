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


class InlineResponse2002DebateRecordCounts(object):
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
        'debate_section_count': 'int',
        'contributor_count': 'int',
        'division_count': 'int',
        'question_count': 'int',
        'bill_count': 'int'
    }

    attribute_map = {
        'debate_section_count': 'debateSectionCount',
        'contributor_count': 'contributorCount',
        'division_count': 'divisionCount',
        'question_count': 'questionCount',
        'bill_count': 'billCount'
    }

    def __init__(self, debate_section_count=None, contributor_count=None, division_count=None, question_count=None, bill_count=None, _configuration=None):  # noqa: E501
        """InlineResponse2002DebateRecordCounts - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._debate_section_count = None
        self._contributor_count = None
        self._division_count = None
        self._question_count = None
        self._bill_count = None
        self.discriminator = None

        self.debate_section_count = debate_section_count
        self.contributor_count = contributor_count
        self.division_count = division_count
        self.question_count = question_count
        self.bill_count = bill_count

    @property
    def debate_section_count(self):
        """Gets the debate_section_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501


        :return: The debate_section_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :rtype: int
        """
        return self._debate_section_count

    @debate_section_count.setter
    def debate_section_count(self, debate_section_count):
        """Sets the debate_section_count of this InlineResponse2002DebateRecordCounts.


        :param debate_section_count: The debate_section_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and debate_section_count is None:
            raise ValueError("Invalid value for `debate_section_count`, must not be `None`")  # noqa: E501

        self._debate_section_count = debate_section_count

    @property
    def contributor_count(self):
        """Gets the contributor_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501


        :return: The contributor_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :rtype: int
        """
        return self._contributor_count

    @contributor_count.setter
    def contributor_count(self, contributor_count):
        """Sets the contributor_count of this InlineResponse2002DebateRecordCounts.


        :param contributor_count: The contributor_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and contributor_count is None:
            raise ValueError("Invalid value for `contributor_count`, must not be `None`")  # noqa: E501

        self._contributor_count = contributor_count

    @property
    def division_count(self):
        """Gets the division_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501


        :return: The division_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :rtype: int
        """
        return self._division_count

    @division_count.setter
    def division_count(self, division_count):
        """Sets the division_count of this InlineResponse2002DebateRecordCounts.


        :param division_count: The division_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and division_count is None:
            raise ValueError("Invalid value for `division_count`, must not be `None`")  # noqa: E501

        self._division_count = division_count

    @property
    def question_count(self):
        """Gets the question_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501


        :return: The question_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :rtype: int
        """
        return self._question_count

    @question_count.setter
    def question_count(self, question_count):
        """Sets the question_count of this InlineResponse2002DebateRecordCounts.


        :param question_count: The question_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and question_count is None:
            raise ValueError("Invalid value for `question_count`, must not be `None`")  # noqa: E501

        self._question_count = question_count

    @property
    def bill_count(self):
        """Gets the bill_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501


        :return: The bill_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :rtype: int
        """
        return self._bill_count

    @bill_count.setter
    def bill_count(self, bill_count):
        """Sets the bill_count of this InlineResponse2002DebateRecordCounts.


        :param bill_count: The bill_count of this InlineResponse2002DebateRecordCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and bill_count is None:
            raise ValueError("Invalid value for `bill_count`, must not be `None`")  # noqa: E501

        self._bill_count = bill_count

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
        if issubclass(InlineResponse2002DebateRecordCounts, dict):
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
        if not isinstance(other, InlineResponse2002DebateRecordCounts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2002DebateRecordCounts):
            return True

        return self.to_dict() != other.to_dict()
