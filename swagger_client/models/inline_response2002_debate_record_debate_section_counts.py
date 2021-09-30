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


class InlineResponse2002DebateRecordDebateSectionCounts(object):
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
        'speech_count': 'int',
        'speaker_count': 'int'
    }

    attribute_map = {
        'speech_count': 'speechCount',
        'speaker_count': 'speakerCount'
    }

    def __init__(self, speech_count=None, speaker_count=None, _configuration=None):  # noqa: E501
        """InlineResponse2002DebateRecordDebateSectionCounts - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._speech_count = None
        self._speaker_count = None
        self.discriminator = None

        self.speech_count = speech_count
        self.speaker_count = speaker_count

    @property
    def speech_count(self):
        """Gets the speech_count of this InlineResponse2002DebateRecordDebateSectionCounts.  # noqa: E501


        :return: The speech_count of this InlineResponse2002DebateRecordDebateSectionCounts.  # noqa: E501
        :rtype: int
        """
        return self._speech_count

    @speech_count.setter
    def speech_count(self, speech_count):
        """Sets the speech_count of this InlineResponse2002DebateRecordDebateSectionCounts.


        :param speech_count: The speech_count of this InlineResponse2002DebateRecordDebateSectionCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and speech_count is None:
            raise ValueError("Invalid value for `speech_count`, must not be `None`")  # noqa: E501

        self._speech_count = speech_count

    @property
    def speaker_count(self):
        """Gets the speaker_count of this InlineResponse2002DebateRecordDebateSectionCounts.  # noqa: E501


        :return: The speaker_count of this InlineResponse2002DebateRecordDebateSectionCounts.  # noqa: E501
        :rtype: int
        """
        return self._speaker_count

    @speaker_count.setter
    def speaker_count(self, speaker_count):
        """Sets the speaker_count of this InlineResponse2002DebateRecordDebateSectionCounts.


        :param speaker_count: The speaker_count of this InlineResponse2002DebateRecordDebateSectionCounts.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and speaker_count is None:
            raise ValueError("Invalid value for `speaker_count`, must not be `None`")  # noqa: E501

        self._speaker_count = speaker_count

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
        if issubclass(InlineResponse2002DebateRecordDebateSectionCounts, dict):
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
        if not isinstance(other, InlineResponse2002DebateRecordDebateSectionCounts):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2002DebateRecordDebateSectionCounts):
            return True

        return self.to_dict() != other.to_dict()
