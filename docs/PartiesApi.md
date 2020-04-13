# oireachtas_api.PartiesApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parties**](PartiesApi.md#parties) | **GET** /parties | Parties List


# **parties**
> object parties(chamber_id=chamber_id, chamber=chamber, house_no=house_no, skip=skip, limit=limit)

Parties List

Returns list of parties filtered by the base and additional parameters. The list supports paging. #### Mapping * Skip - Equal To - this will ignore the first x number of records set in the parameter * Limit - Equal To - this will only return a specific amount of records * House/Chamber - house.house.uri 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.PartiesApi()
chamber_id = ['[]'] # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
chamber = '' # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
house_no = 56 # int | filter by house number (optional)
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)

try:
    # Parties List
    api_response = api_instance.parties(chamber_id=chamber_id, chamber=chamber, house_no=house_no, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartiesApi->parties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | [**list[str]**](str.md)| Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  | [optional] [default to []]
 **chamber** | **str**| Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  | [optional] [default to ]
 **house_no** | **int**| filter by house number | [optional] 
 **skip** | **int**| This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. | [optional] [default to 0]
 **limit** | **int**| This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. | [optional] [default to 50]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

