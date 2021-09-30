# coding: utf-8

# flake8: noqa
"""
    Houses of the Oireachtas Open Data APIs

    The Houses of the Oireachtas is providing these APIs to allow our datasets to be retrieved and reused as widely as possible. They are intended to be used in conjunction with https://data.oireachtas.ie, from where our datasets can be accessed directly. By using the APIs, users can make metadata queries to identify the specific data they require. New data are available through the API as soon as they are published.  Currently, https://data.oireachtas.ie contains data in XML format from the Official Report of the Houses of the Oireachtas (the \"debates\") and replies to Parliamentary Questions in XML files complying with the [Akoma Ntoso](http://akomantoso.org) schema, as well data in PDF format for Bills, Acts and other documents published by the Houses of the Oireachtas.  Files can be retrieved from https://data.oireachtas.ie by adding the URI fragment contained in the \"formats\" fields of the JSON documents returned by these APIs. At the moment only PDF and XML files are available directly from https://data.oireachtas.ie, but this will become the endpoint for direct access of all \"uri\" fields in the data queried through https://api.oireachtas.ie. We will also be making bulk downloads available through https://data.oireachtas.ie.  Please note the APIs are a work in progress. We are working on expanding the range of datasets we publish, and we are interested in hearing about how to make these APIs more useful and wide ranging. For these reasons, we welcome any feedback, suggestions and user stories to open.data@oireachtas.ie  Data published through these APIs are made available under the [Oireachtas (Open Data) PSI Licence](https://beta.oireachtas.ie/en/open-data/license/)  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: open.data@oireachtas.ie
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from swagger_client.models.error_response import ErrorResponse
from swagger_client.models.inline_response200 import InlineResponse200
from swagger_client.models.inline_response2001 import InlineResponse2001
from swagger_client.models.inline_response2001_question import InlineResponse2001Question
from swagger_client.models.inline_response2001_question_by import InlineResponse2001QuestionBy
from swagger_client.models.inline_response2001_question_debate_section import InlineResponse2001QuestionDebateSection
from swagger_client.models.inline_response2001_question_debate_section_formats import InlineResponse2001QuestionDebateSectionFormats
from swagger_client.models.inline_response2001_question_to import InlineResponse2001QuestionTo
from swagger_client.models.inline_response2001_results import InlineResponse2001Results
from swagger_client.models.inline_response2002 import InlineResponse2002
from swagger_client.models.inline_response2002_debate_record import InlineResponse2002DebateRecord
from swagger_client.models.inline_response2002_debate_record_chamber import InlineResponse2002DebateRecordChamber
from swagger_client.models.inline_response2002_debate_record_counts import InlineResponse2002DebateRecordCounts
from swagger_client.models.inline_response2002_debate_record_debate_section import InlineResponse2002DebateRecordDebateSection
from swagger_client.models.inline_response2002_debate_record_debate_section_counts import InlineResponse2002DebateRecordDebateSectionCounts
from swagger_client.models.inline_response2002_debate_record_debate_section_speakers import InlineResponse2002DebateRecordDebateSectionSpeakers
from swagger_client.models.inline_response2002_debate_record_debate_sections import InlineResponse2002DebateRecordDebateSections
from swagger_client.models.inline_response2002_debate_record_house import InlineResponse2002DebateRecordHouse
from swagger_client.models.inline_response2002_results import InlineResponse2002Results
from swagger_client.models.inline_response2003 import InlineResponse2003
from swagger_client.models.inline_response2003_division import InlineResponse2003Division
from swagger_client.models.inline_response2003_division_debate import InlineResponse2003DivisionDebate
from swagger_client.models.inline_response2003_division_house import InlineResponse2003DivisionHouse
from swagger_client.models.inline_response2003_division_subject import InlineResponse2003DivisionSubject
from swagger_client.models.inline_response2003_division_tallies import InlineResponse2003DivisionTallies
from swagger_client.models.inline_response2003_results import InlineResponse2003Results
from swagger_client.models.inline_response2004 import InlineResponse2004
from swagger_client.models.inline_response2004_head import InlineResponse2004Head
from swagger_client.models.inline_response2004_head_counts import InlineResponse2004HeadCounts
from swagger_client.models.inline_response2004_head_date_range import InlineResponse2004HeadDateRange
from swagger_client.models.inline_response2004_member import InlineResponse2004Member
from swagger_client.models.inline_response2004_member_membership import InlineResponse2004MemberMembership
from swagger_client.models.inline_response2004_member_membership_house import InlineResponse2004MemberMembershipHouse
from swagger_client.models.inline_response2004_member_membership_office import InlineResponse2004MemberMembershipOffice
from swagger_client.models.inline_response2004_member_membership_office_date_range import InlineResponse2004MemberMembershipOfficeDateRange
from swagger_client.models.inline_response2004_member_membership_office_office_name import InlineResponse2004MemberMembershipOfficeOfficeName
from swagger_client.models.inline_response2004_member_membership_offices import InlineResponse2004MemberMembershipOffices
from swagger_client.models.inline_response2004_member_membership_parties import InlineResponse2004MemberMembershipParties
from swagger_client.models.inline_response2004_member_membership_party import InlineResponse2004MemberMembershipParty
from swagger_client.models.inline_response2004_member_membership_party_date_range import InlineResponse2004MemberMembershipPartyDateRange
from swagger_client.models.inline_response2004_member_membership_represent import InlineResponse2004MemberMembershipRepresent
from swagger_client.models.inline_response2004_member_membership_represents import InlineResponse2004MemberMembershipRepresents
from swagger_client.models.inline_response2004_member_memberships import InlineResponse2004MemberMemberships
from swagger_client.models.inline_response2004_results import InlineResponse2004Results
from swagger_client.models.inline_response200_bill import InlineResponse200Bill
from swagger_client.models.inline_response200_bill_amendment_lists import InlineResponse200BillAmendmentLists
from swagger_client.models.inline_response200_bill_origin_house import InlineResponse200BillOriginHouse
from swagger_client.models.inline_response200_bill_stages import InlineResponse200BillStages
from swagger_client.models.inline_response200_bill_version import InlineResponse200BillVersion
from swagger_client.models.inline_response200_bill_versions import InlineResponse200BillVersions
from swagger_client.models.inline_response200_head import InlineResponse200Head
from swagger_client.models.inline_response200_head_date_range import InlineResponse200HeadDateRange
from swagger_client.models.inline_response200_results import InlineResponse200Results