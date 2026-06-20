# coding: utf-8

import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from oireachtas_api.configuration import Configuration
from oireachtas_api.api_client import ApiClient
from oireachtas_api.api.constituencies_api import ConstituenciesApi
from oireachtas_api.api.debates_api import DebatesApi
from oireachtas_api.api.divisions_api import DivisionsApi
from oireachtas_api.api.houses_api import HousesApi
from oireachtas_api.api.legislation_api import LegislationApi
from oireachtas_api.api.members_api import MembersApi
from oireachtas_api.api.parties_api import PartiesApi
from oireachtas_api.api.questions_api import QuestionsApi


class Client:
    """A simplified, unified client wrapper for the Houses of the Oireachtas Open Data APIs."""

    def __init__(
        self,
        host: Optional[str] = None,
        debug: bool = False,
        verify_ssl: bool = True,
        proxy: Optional[str] = None,
        timeout: Optional[Union[int, float, Tuple[Union[int, float], Union[int, float]]]] = None,
        api_client: Optional[ApiClient] = None,
    ):
        """Initialize the unified Oireachtas API Client.

        :param host: Optional custom API host URL (defaults to "https://api.oireachtas.ie/v1").
        :param debug: Set to True to enable debug logging.
        :param verify_ssl: Set to False to disable SSL certificate verification.
        :param proxy: Optional proxy URL (e.g., "http://localhost:3128").
        :param timeout: Optional timeout setting. Can be a number (total timeout) or a tuple (connect, read).
        :param api_client: Optional pre-configured ApiClient instance to reuse.
        """
        if api_client is not None:
            self.api_client = api_client
            self.configuration = api_client.configuration
        else:
            self.configuration = Configuration()
            if host:
                self.configuration.host = host
            self.configuration.debug = debug
            self.configuration.verify_ssl = verify_ssl
            if proxy:
                self.configuration.proxy = proxy

            self.api_client = ApiClient(self.configuration)

        if timeout is not None:
            # We configure default timeout for request execution if provided
            # The underlying OpenAPI generated methods allow overriding via _request_timeout
            self._default_timeout = timeout
        else:
            self._default_timeout = None

        # Initialize underlying Swagger API wrappers
        self._constituencies_api = ConstituenciesApi(self.api_client)
        self._debates_api = DebatesApi(self.api_client)
        self._divisions_api = DivisionsApi(self.api_client)
        self._houses_api = HousesApi(self.api_client)
        self._legislation_api = LegislationApi(self.api_client)
        self._members_api = MembersApi(self.api_client)
        self._parties_api = PartiesApi(self.api_client)
        self._questions_api = QuestionsApi(self.api_client)

    def _to_dict_or_raw(self, obj: Any) -> Any:
        """Recursively convert OpenAPI models to standard Python dictionaries/lists."""
        if hasattr(obj, "to_dict"):
            return obj.to_dict()
        elif isinstance(obj, list):
            return [self._to_dict_or_raw(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: self._to_dict_or_raw(v) for k, v in obj.items()}
        return obj

    def _prepare_kwargs(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Inject default timeout and other global configurations into kwargs if not overridden."""
        if self._default_timeout is not None and "_request_timeout" not in kwargs:
            kwargs["_request_timeout"] = self._default_timeout
        return kwargs

    def constituencies(
        self,
        chamber_id: Optional[List[str]] = None,
        chamber: Optional[str] = None,
        house_no: Optional[int] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs: Any
    ) -> Any:
        """Retrieve electoral districts.

        :param chamber_id: Filter by house or committee uri (e.g. ['/ie/oireachtas/house/dail/32']).
        :param chamber: Filter by House name ('dail' or 'seanad').
        :param house_no: Filter by house number.
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing constituencies data.
        """
        params = {
            "chamber_id": chamber_id,
            "chamber": chamber,
            "house_no": house_no,
            "skip": skip,
            "limit": limit,
        }
        # Filter out None values to prevent overriding defaults
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._constituencies_api.constituencies(**kwargs)
        return self._to_dict_or_raw(res)

    def debates(
        self,
        chamber_type: Optional[str] = None,
        chamber_id: Optional[List[str]] = None,
        chamber: Optional[str] = None,
        date_start: Optional[Union[datetime.date, str]] = None,
        date_end: Optional[Union[datetime.date, str]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        member_id: Optional[str] = None,
        debate_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """Access official debates transcripts.

        :param chamber_type: Filter results by House (Dáil, Seanad, or committees).
        :param chamber_id: Filter by house or committee uri.
        :param chamber: Filter by House name ('dail' or 'seanad').
        :param date_start: Filter by start date (datetime.date or 'YYYY-MM-DD').
        :param date_end: Filter by end date (datetime.date or 'YYYY-MM-DD').
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param member_id: Filter by Member uri.
        :param debate_id: Filter by debate uri.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing debates data.
        """
        params = {
            "chamber_type": chamber_type,
            "chamber_id": chamber_id,
            "chamber": chamber,
            "date_start": date_start,
            "date_end": date_end,
            "skip": skip,
            "limit": limit,
            "member_id": member_id,
            "debate_id": debate_id,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._debates_api.debates(**kwargs)
        return self._to_dict_or_raw(res)

    def divisions(
        self,
        chamber_type: Optional[str] = None,
        chamber_id: Optional[List[str]] = None,
        chamber: Optional[str] = None,
        date_start: Optional[Union[datetime.date, str]] = None,
        date_end: Optional[Union[datetime.date, str]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        outcome: Optional[List[str]] = None,
        member_id: Optional[str] = None,
        debate_id: Optional[str] = None,
        vote_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """Inspect parliamentary votes and counts.

        :param chamber_type: Filter results by House (Dáil, Seanad, or committees).
        :param chamber_id: Filter by house or committee uri.
        :param chamber: Filter by House name ('dail' or 'seanad').
        :param date_start: Filter by start date (datetime.date or 'YYYY-MM-DD').
        :param date_end: Filter by end date (datetime.date or 'YYYY-MM-DD').
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param outcome: Filter divisions by outcome.
        :param member_id: Filter by Member uri.
        :param debate_id: Filter by debate uri.
        :param vote_id: Division Identifier for a Single Division.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing divisions data.
        """
        params = {
            "chamber_type": chamber_type,
            "chamber_id": chamber_id,
            "chamber": chamber,
            "date_start": date_start,
            "date_end": date_end,
            "skip": skip,
            "limit": limit,
            "outcome": outcome,
            "member_id": member_id,
            "debate_id": debate_id,
            "vote_id": vote_id,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._divisions_api.divisions(**kwargs)
        return self._to_dict_or_raw(res)

    def houses(
        self,
        chamber_id: Optional[List[str]] = None,
        chamber: Optional[str] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs: Any
    ) -> Any:
        """Query house info (Dáil or Seanad).

        :param chamber_id: Filter by house or committee uri.
        :param chamber: Filter by House name ('dail' or 'seanad').
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing houses data.
        """
        params = {
            "chamber_id": chamber_id,
            "chamber": chamber,
            "skip": skip,
            "limit": limit,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._houses_api.houses(**kwargs)
        return self._to_dict_or_raw(res)

    def legislation(
        self,
        bill_status: Optional[List[str]] = None,
        bill_source: Optional[List[str]] = None,
        date_start: Optional[Union[datetime.date, str]] = None,
        date_end: Optional[Union[datetime.date, str]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        member_id: Optional[str] = None,
        bill_id: Optional[str] = None,
        bill_no: Optional[str] = None,
        bill_year: Optional[str] = None,
        chamber_id: Optional[List[str]] = None,
        act_year: Optional[str] = None,
        act_no: Optional[str] = None,
        lang: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """Query active and historic bills and acts.

        :param bill_status: Filter legislation by status (e.g. ['Current', 'Enacted']).
        :param bill_source: Filter legislation by origin source.
        :param date_start: Filter by start date.
        :param date_end: Filter by end date.
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param member_id: Filter by Member uri.
        :param bill_id: Filter results by Bill URI (e.g. '/ie/oireachtas/bill/2016/2').
        :param bill_no: Filter Bill by number.
        :param bill_year: Filter Bill by year.
        :param chamber_id: Filter by house or committee uri.
        :param act_year: Filter Bill by Act year.
        :param act_no: Filter Bill by Act number.
        :param lang: Language of document to extract. Defaults to English ('en').
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing legislation data.
        """
        params = {
            "bill_status": bill_status,
            "bill_source": bill_source,
            "date_start": date_start,
            "date_end": date_end,
            "skip": skip,
            "limit": limit,
            "member_id": member_id,
            "bill_id": bill_id,
            "bill_no": bill_no,
            "bill_year": bill_year,
            "chamber_id": chamber_id,
            "act_year": act_year,
            "act_no": act_no,
            "lang": lang,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._legislation_api.legislation(**kwargs)
        return self._to_dict_or_raw(res)

    def members(
        self,
        date_start: Optional[Union[datetime.date, str]] = None,
        chamber_id: Optional[List[str]] = None,
        chamber: Optional[str] = None,
        house_no: Optional[int] = None,
        member_id: Optional[str] = None,
        date_end: Optional[Union[datetime.date, str]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        party_code: Optional[str] = None,
        party_id: Optional[str] = None,
        const_code: Optional[str] = None,
        const_id: Optional[str] = None,
        **kwargs: Any
    ) -> Any:
        """Look up details of TDs and Senators.

        :param date_start: Filter by membership start date.
        :param chamber_id: Filter by house or committee uri.
        :param chamber: Filter by House name ('dail' or 'seanad').
        :param house_no: Filter by house number.
        :param member_id: Filter by Member uri.
        :param date_end: Filter by membership end date.
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param party_code: Filter by party code.
        :param party_id: Filter by party uri.
        :param const_code: Filter by constituency code.
        :param const_id: Filter by constituency uri.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing members data.
        """
        params = {
            "date_start": date_start,
            "chamber_id": chamber_id,
            "chamber": chamber,
            "house_no": house_no,
            "member_id": member_id,
            "date_end": date_end,
            "skip": skip,
            "limit": limit,
            "party_code": party_code,
            "party_id": party_id,
            "const_code": const_code,
            "const_id": const_id,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._members_api.members(**kwargs)
        return self._to_dict_or_raw(res)

    def parties(
        self,
        chamber_id: Optional[List[str]] = None,
        chamber: Optional[str] = None,
        house_no: Optional[int] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs: Any
    ) -> Any:
        """List political parties.

        :param chamber_id: Filter by house or committee uri.
        :param chamber: Filter by House name ('dail' or 'seanad').
        :param house_no: Filter by house number.
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing parties data.
        """
        params = {
            "chamber_id": chamber_id,
            "chamber": chamber,
            "house_no": house_no,
            "skip": skip,
            "limit": limit,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._parties_api.parties(**kwargs)
        return self._to_dict_or_raw(res)

    def questions(
        self,
        date_start: Optional[Union[datetime.date, str]] = None,
        date_end: Optional[Union[datetime.date, str]] = None,
        skip: Optional[int] = None,
        limit: Optional[int] = None,
        qtype: Optional[List[str]] = None,
        member_id: Optional[str] = None,
        question_id: Optional[str] = None,
        question_no: Optional[int] = None,
        **kwargs: Any
    ) -> Any:
        """Query parliamentary questions (PQs).

        :param date_start: Filter by start date related to the Section.
        :param date_end: Filter by end date related to the Section.
        :param skip: Number of records to skip.
        :param limit: Maximum number of records to return.
        :param qtype: Filter questions by oral or written ('oral' or 'written').
        :param member_id: Filter by Member uri.
        :param question_id: Identifier for a Single Question.
        :param question_no: Filter by question number.
        :param kwargs: Additional query/request parameters (e.g. async_req=True).
        :return: Standard Python list/dict containing questions data.
        """
        params = {
            "date_start": date_start,
            "date_end": date_end,
            "skip": skip,
            "limit": limit,
            "qtype": qtype,
            "member_id": member_id,
            "question_id": question_id,
            "question_no": question_no,
        }
        filtered_params = {k: v for k, v in params.items() if v is not None}
        kwargs.update(filtered_params)
        kwargs = self._prepare_kwargs(kwargs)

        res = self._questions_api.questions(**kwargs)
        return self._to_dict_or_raw(res)
