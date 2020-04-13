# oireachtas_api.DivisionsApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**divisions**](DivisionsApi.md#divisions) | **GET** /divisions | Divisions


# **divisions**
> InlineResponse2003 divisions(chamber_type=chamber_type, chamber_id=chamber_id, chamber=chamber, date_start=date_start, date_end=date_end, skip=skip, limit=limit, outcome=outcome, member_id=member_id, debate_id=debate_id, vote_id=vote_id)

Divisions

This will return a list of divisions which meet certain criteria #### Indexes * division_meta  #### Mapping * Division outcome - Equal To - division.outcome * Start Date - Greater than or Equal To - division.date * End Date - Greater than or Equal To - division.date 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.DivisionsApi()
chamber_type = 'chamber_type_example' # str | Filter results by House, ie, Dáil or Seanad or committees.  (optional)
chamber_id = ['[]'] # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
chamber = '' # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
date_start = '1900-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
date_end = '2099-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
outcome = ['[]'] # list[str] | Filter divisions by outcome (optional) (default to [])
member_id = 'member_id_example' # str | Filter by Member uri. (optional)
debate_id = 'debate_id_example' # str | Filter by debate uri (optional)
vote_id = 'vote_id_example' # str | Division Identifier for a Single Division (optional)

try:
    # Divisions
    api_response = api_instance.divisions(chamber_type=chamber_type, chamber_id=chamber_id, chamber=chamber, date_start=date_start, date_end=date_end, skip=skip, limit=limit, outcome=outcome, member_id=member_id, debate_id=debate_id, vote_id=vote_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DivisionsApi->divisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_type** | **str**| Filter results by House, ie, Dáil or Seanad or committees.  | [optional] 
 **chamber_id** | [**list[str]**](str.md)| Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  | [optional] [default to []]
 **chamber** | **str**| Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  | [optional] [default to ]
 **date_start** | **date**| This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. | [optional] [default to 1900-01-01]
 **date_end** | **date**| This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. | [optional] [default to 2099-01-01]
 **skip** | **int**| This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. | [optional] [default to 0]
 **limit** | **int**| This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. | [optional] [default to 50]
 **outcome** | [**list[str]**](str.md)| Filter divisions by outcome | [optional] [default to []]
 **member_id** | **str**| Filter by Member uri. | [optional] 
 **debate_id** | **str**| Filter by debate uri | [optional] 
 **vote_id** | **str**| Division Identifier for a Single Division | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

