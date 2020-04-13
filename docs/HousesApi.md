# oireachtas_api.HousesApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**houses**](HousesApi.md#houses) | **GET** /houses | Houses


# **houses**
> object houses(chamber_id=chamber_id, chamber=chamber, skip=skip, limit=limit)

Houses

Returns a house. #### Indexes * houses  #### Mapping * House ID - Equal To - house.houseCode 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.HousesApi()
chamber_id = ['[]'] # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
chamber = '' # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)

try:
    # Houses
    api_response = api_instance.houses(chamber_id=chamber_id, chamber=chamber, skip=skip, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HousesApi->houses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chamber_id** | [**list[str]**](str.md)| Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  | [optional] [default to []]
 **chamber** | **str**| Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  | [optional] [default to ]
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

