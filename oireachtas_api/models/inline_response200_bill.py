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


class InlineResponse200Bill(object):
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
        'debates': 'list[Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionsdebate]',
        'sponsors': 'list[Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionssponsor]',
        'last_updated': 'datetime',
        'long_title_en': 'object',
        'long_title_ga': 'object',
        'origin_house': 'InlineResponse200BillOriginHouse',
        'short_title_en': 'str',
        'short_title_ga': 'str',
        'status': 'str',
        'bill_type': 'str',
        'events': 'list[object]',
        'most_recent_stage': 'object',
        'uri': 'str',
        'act': 'Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionsAct',
        'amendment_lists': 'list[InlineResponse200BillAmendmentLists]',
        'bill_year': 'str',
        'related_docs': 'list[object]',
        'bill_no': 'str',
        'stages': 'list[InlineResponse200BillStages]',
        'method': 'str',
        'source': 'str',
        'versions': 'list[InlineResponse200BillVersions]'
    }

    attribute_map = {
        'debates': 'debates',
        'sponsors': 'sponsors',
        'last_updated': 'lastUpdated',
        'long_title_en': 'longTitleEn',
        'long_title_ga': 'longTitleGa',
        'origin_house': 'originHouse',
        'short_title_en': 'shortTitleEn',
        'short_title_ga': 'shortTitleGa',
        'status': 'status',
        'bill_type': 'billType',
        'events': 'events',
        'most_recent_stage': 'mostRecentStage',
        'uri': 'uri',
        'act': 'act',
        'amendment_lists': 'amendmentLists',
        'bill_year': 'billYear',
        'related_docs': 'relatedDocs',
        'bill_no': 'billNo',
        'stages': 'stages',
        'method': 'method',
        'source': 'source',
        'versions': 'versions'
    }

    def __init__(self, debates=None, sponsors=None, last_updated=None, long_title_en=None, long_title_ga=None, origin_house=None, short_title_en=None, short_title_ga=None, status=None, bill_type=None, events=None, most_recent_stage=None, uri=None, act=None, amendment_lists=None, bill_year=None, related_docs=None, bill_no=None, stages=None, method=None, source=None, versions=None):  # noqa: E501
        """InlineResponse200Bill - a model defined in Swagger"""  # noqa: E501

        self._debates = None
        self._sponsors = None
        self._last_updated = None
        self._long_title_en = None
        self._long_title_ga = None
        self._origin_house = None
        self._short_title_en = None
        self._short_title_ga = None
        self._status = None
        self._bill_type = None
        self._events = None
        self._most_recent_stage = None
        self._uri = None
        self._act = None
        self._amendment_lists = None
        self._bill_year = None
        self._related_docs = None
        self._bill_no = None
        self._stages = None
        self._method = None
        self._source = None
        self._versions = None
        self.discriminator = None

        self.debates = debates
        self.sponsors = sponsors
        self.last_updated = last_updated
        self.long_title_en = long_title_en
        self.long_title_ga = long_title_ga
        self.origin_house = origin_house
        self.short_title_en = short_title_en
        self.short_title_ga = short_title_ga
        self.status = status
        self.bill_type = bill_type
        self.events = events
        self.most_recent_stage = most_recent_stage
        self.uri = uri
        self.act = act
        self.amendment_lists = amendment_lists
        self.bill_year = bill_year
        self.related_docs = related_docs
        self.bill_no = bill_no
        self.stages = stages
        self.method = method
        self.source = source
        self.versions = versions

    @property
    def debates(self):
        """Gets the debates of this InlineResponse200Bill.  # noqa: E501


        :return: The debates of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionsdebate]
        """
        return self._debates

    @debates.setter
    def debates(self, debates):
        """Sets the debates of this InlineResponse200Bill.


        :param debates: The debates of this InlineResponse200Bill.  # noqa: E501
        :type: list[Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionsdebate]
        """
        if debates is None:
            raise ValueError("Invalid value for `debates`, must not be `None`")  # noqa: E501

        self._debates = debates

    @property
    def sponsors(self):
        """Gets the sponsors of this InlineResponse200Bill.  # noqa: E501


        :return: The sponsors of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionssponsor]
        """
        return self._sponsors

    @sponsors.setter
    def sponsors(self, sponsors):
        """Sets the sponsors of this InlineResponse200Bill.


        :param sponsors: The sponsors of this InlineResponse200Bill.  # noqa: E501
        :type: list[Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionssponsor]
        """
        if sponsors is None:
            raise ValueError("Invalid value for `sponsors`, must not be `None`")  # noqa: E501

        self._sponsors = sponsors

    @property
    def last_updated(self):
        """Gets the last_updated of this InlineResponse200Bill.  # noqa: E501


        :return: The last_updated of this InlineResponse200Bill.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this InlineResponse200Bill.


        :param last_updated: The last_updated of this InlineResponse200Bill.  # noqa: E501
        :type: datetime
        """
        if last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def long_title_en(self):
        """Gets the long_title_en of this InlineResponse200Bill.  # noqa: E501


        :return: The long_title_en of this InlineResponse200Bill.  # noqa: E501
        :rtype: object
        """
        return self._long_title_en

    @long_title_en.setter
    def long_title_en(self, long_title_en):
        """Sets the long_title_en of this InlineResponse200Bill.


        :param long_title_en: The long_title_en of this InlineResponse200Bill.  # noqa: E501
        :type: object
        """
        if long_title_en is None:
            raise ValueError("Invalid value for `long_title_en`, must not be `None`")  # noqa: E501

        self._long_title_en = long_title_en

    @property
    def long_title_ga(self):
        """Gets the long_title_ga of this InlineResponse200Bill.  # noqa: E501


        :return: The long_title_ga of this InlineResponse200Bill.  # noqa: E501
        :rtype: object
        """
        return self._long_title_ga

    @long_title_ga.setter
    def long_title_ga(self, long_title_ga):
        """Sets the long_title_ga of this InlineResponse200Bill.


        :param long_title_ga: The long_title_ga of this InlineResponse200Bill.  # noqa: E501
        :type: object
        """
        if long_title_ga is None:
            raise ValueError("Invalid value for `long_title_ga`, must not be `None`")  # noqa: E501

        self._long_title_ga = long_title_ga

    @property
    def origin_house(self):
        """Gets the origin_house of this InlineResponse200Bill.  # noqa: E501


        :return: The origin_house of this InlineResponse200Bill.  # noqa: E501
        :rtype: InlineResponse200BillOriginHouse
        """
        return self._origin_house

    @origin_house.setter
    def origin_house(self, origin_house):
        """Sets the origin_house of this InlineResponse200Bill.


        :param origin_house: The origin_house of this InlineResponse200Bill.  # noqa: E501
        :type: InlineResponse200BillOriginHouse
        """
        if origin_house is None:
            raise ValueError("Invalid value for `origin_house`, must not be `None`")  # noqa: E501

        self._origin_house = origin_house

    @property
    def short_title_en(self):
        """Gets the short_title_en of this InlineResponse200Bill.  # noqa: E501


        :return: The short_title_en of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._short_title_en

    @short_title_en.setter
    def short_title_en(self, short_title_en):
        """Sets the short_title_en of this InlineResponse200Bill.


        :param short_title_en: The short_title_en of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if short_title_en is None:
            raise ValueError("Invalid value for `short_title_en`, must not be `None`")  # noqa: E501

        self._short_title_en = short_title_en

    @property
    def short_title_ga(self):
        """Gets the short_title_ga of this InlineResponse200Bill.  # noqa: E501


        :return: The short_title_ga of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._short_title_ga

    @short_title_ga.setter
    def short_title_ga(self, short_title_ga):
        """Sets the short_title_ga of this InlineResponse200Bill.


        :param short_title_ga: The short_title_ga of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if short_title_ga is None:
            raise ValueError("Invalid value for `short_title_ga`, must not be `None`")  # noqa: E501

        self._short_title_ga = short_title_ga

    @property
    def status(self):
        """Gets the status of this InlineResponse200Bill.  # noqa: E501


        :return: The status of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse200Bill.


        :param status: The status of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Defeated", "Enacted", "Lapsed", "Current", "Withdrawn", "Rejected"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def bill_type(self):
        """Gets the bill_type of this InlineResponse200Bill.  # noqa: E501


        :return: The bill_type of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this InlineResponse200Bill.


        :param bill_type: The bill_type of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if bill_type is None:
            raise ValueError("Invalid value for `bill_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Public", "Private", "Hybrid"]  # noqa: E501
        if bill_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bill_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bill_type, allowed_values)
            )

        self._bill_type = bill_type

    @property
    def events(self):
        """Gets the events of this InlineResponse200Bill.  # noqa: E501


        :return: The events of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[object]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this InlineResponse200Bill.


        :param events: The events of this InlineResponse200Bill.  # noqa: E501
        :type: list[object]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501

        self._events = events

    @property
    def most_recent_stage(self):
        """Gets the most_recent_stage of this InlineResponse200Bill.  # noqa: E501


        :return: The most_recent_stage of this InlineResponse200Bill.  # noqa: E501
        :rtype: object
        """
        return self._most_recent_stage

    @most_recent_stage.setter
    def most_recent_stage(self, most_recent_stage):
        """Sets the most_recent_stage of this InlineResponse200Bill.


        :param most_recent_stage: The most_recent_stage of this InlineResponse200Bill.  # noqa: E501
        :type: object
        """
        if most_recent_stage is None:
            raise ValueError("Invalid value for `most_recent_stage`, must not be `None`")  # noqa: E501

        self._most_recent_stage = most_recent_stage

    @property
    def uri(self):
        """Gets the uri of this InlineResponse200Bill.  # noqa: E501


        :return: The uri of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this InlineResponse200Bill.


        :param uri: The uri of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501

        self._uri = uri

    @property
    def act(self):
        """Gets the act of this InlineResponse200Bill.  # noqa: E501


        :return: The act of this InlineResponse200Bill.  # noqa: E501
        :rtype: Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionsAct
        """
        return self._act

    @act.setter
    def act(self, act):
        """Sets the act of this InlineResponse200Bill.


        :param act: The act of this InlineResponse200Bill.  # noqa: E501
        :type: Paths1legislationgetresponses200schemapropertiesresultsitemsdefinitionsAct
        """
        if act is None:
            raise ValueError("Invalid value for `act`, must not be `None`")  # noqa: E501

        self._act = act

    @property
    def amendment_lists(self):
        """Gets the amendment_lists of this InlineResponse200Bill.  # noqa: E501


        :return: The amendment_lists of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[InlineResponse200BillAmendmentLists]
        """
        return self._amendment_lists

    @amendment_lists.setter
    def amendment_lists(self, amendment_lists):
        """Sets the amendment_lists of this InlineResponse200Bill.


        :param amendment_lists: The amendment_lists of this InlineResponse200Bill.  # noqa: E501
        :type: list[InlineResponse200BillAmendmentLists]
        """
        if amendment_lists is None:
            raise ValueError("Invalid value for `amendment_lists`, must not be `None`")  # noqa: E501

        self._amendment_lists = amendment_lists

    @property
    def bill_year(self):
        """Gets the bill_year of this InlineResponse200Bill.  # noqa: E501


        :return: The bill_year of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._bill_year

    @bill_year.setter
    def bill_year(self, bill_year):
        """Sets the bill_year of this InlineResponse200Bill.


        :param bill_year: The bill_year of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if bill_year is None:
            raise ValueError("Invalid value for `bill_year`, must not be `None`")  # noqa: E501

        self._bill_year = bill_year

    @property
    def related_docs(self):
        """Gets the related_docs of this InlineResponse200Bill.  # noqa: E501


        :return: The related_docs of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[object]
        """
        return self._related_docs

    @related_docs.setter
    def related_docs(self, related_docs):
        """Sets the related_docs of this InlineResponse200Bill.


        :param related_docs: The related_docs of this InlineResponse200Bill.  # noqa: E501
        :type: list[object]
        """
        if related_docs is None:
            raise ValueError("Invalid value for `related_docs`, must not be `None`")  # noqa: E501

        self._related_docs = related_docs

    @property
    def bill_no(self):
        """Gets the bill_no of this InlineResponse200Bill.  # noqa: E501


        :return: The bill_no of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._bill_no

    @bill_no.setter
    def bill_no(self, bill_no):
        """Sets the bill_no of this InlineResponse200Bill.


        :param bill_no: The bill_no of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if bill_no is None:
            raise ValueError("Invalid value for `bill_no`, must not be `None`")  # noqa: E501

        self._bill_no = bill_no

    @property
    def stages(self):
        """Gets the stages of this InlineResponse200Bill.  # noqa: E501


        :return: The stages of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[InlineResponse200BillStages]
        """
        return self._stages

    @stages.setter
    def stages(self, stages):
        """Sets the stages of this InlineResponse200Bill.


        :param stages: The stages of this InlineResponse200Bill.  # noqa: E501
        :type: list[InlineResponse200BillStages]
        """
        if stages is None:
            raise ValueError("Invalid value for `stages`, must not be `None`")  # noqa: E501

        self._stages = stages

    @property
    def method(self):
        """Gets the method of this InlineResponse200Bill.  # noqa: E501


        :return: The method of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this InlineResponse200Bill.


        :param method: The method of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def source(self):
        """Gets the source of this InlineResponse200Bill.  # noqa: E501


        :return: The source of this InlineResponse200Bill.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InlineResponse200Bill.


        :param source: The source of this InlineResponse200Bill.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501

        self._source = source

    @property
    def versions(self):
        """Gets the versions of this InlineResponse200Bill.  # noqa: E501


        :return: The versions of this InlineResponse200Bill.  # noqa: E501
        :rtype: list[InlineResponse200BillVersions]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this InlineResponse200Bill.


        :param versions: The versions of this InlineResponse200Bill.  # noqa: E501
        :type: list[InlineResponse200BillVersions]
        """
        if versions is None:
            raise ValueError("Invalid value for `versions`, must not be `None`")  # noqa: E501

        self._versions = versions

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
        if issubclass(InlineResponse200Bill, dict):
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
        if not isinstance(other, InlineResponse200Bill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
