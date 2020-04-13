# oireachtas_api.DebatesApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**debates**](DebatesApi.md#debates) | **GET** /debates | Debates List


# **debates**
> InlineResponse2002 debates(chamber_type=chamber_type, chamber_id=chamber_id, chamber=chamber, date_start=date_start, date_end=date_end, skip=skip, limit=limit, member_id=member_id, debate_id=debate_id)

Debates List

Returns list of debates filtered by the base and additional parameters. The list supports paging. #### Mapping * Start Date - Greater Than or Equal To - debateRecord.date * End Date - Less Than or Equal To - debateRecord.date * Skip - Equal To - this will ignore the first x number of records set in the parameter * Limit - Equal To - this will only return a specific amount of records 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.DebatesApi()
chamber_type = 'chamber_type_example' # str | Filter results by House, ie, Dáil or Seanad or committees.  (optional)
chamber_id = ['[]'] # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
chamber = '' # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
date_start = '1900-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
date_end = '2099-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
member_id = 'member_id_example' # str | Filter by Member uri. (optional)
debate_id = 'debate_id_example' # str | Filter by debate uri (optional)

try:
    # Debates List
    api_response = api_instance.debates(chamber_type=chamber_type, chamber_id=chamber_id, chamber=chamber, date_start=date_start, date_end=date_end, skip=skip, limit=limit, member_id=member_id, debate_id=debate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebatesApi->debates: %s\n" % e)
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
 **member_id** | **str**| Filter by Member uri. | [optional] 
 **debate_id** | **str**| Filter by debate uri | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

