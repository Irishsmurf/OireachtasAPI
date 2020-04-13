# oireachtas_api.MembersApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**members**](MembersApi.md#members) | **GET** /members | Members


# **members**
> InlineResponse2004 members(date_start=date_start, chamber_id=chamber_id, chamber=chamber, house_no=house_no, member_id=member_id, date_end=date_end, skip=skip, limit=limit, party_code=party_code, party_id=party_id, const_code=const_code, const_id=const_id)

Members

Returns a list of members. #### Indexes * members  #### Mapping * Date Start- Greater Than or Equal To - member.memberships.membership.dateRange.start * Date Start- Less Than or Equal To - member.memberships.membership.dateRange.end 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.MembersApi()
date_start = '1900-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
chamber_id = ['[]'] # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
chamber = '' # str | Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  (optional) (default to )
house_no = 56 # int | filter by house number (optional)
member_id = 'member_id_example' # str | Filter by Member uri. (optional)
date_end = '2099-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
party_code = 'party_code_example' # str | Filter by party code (optional)
party_id = 'party_id_example' # str | Filter by unique party identifier (uri) (optional)
const_code = 'const_code_example' # str | Filter by constituency code (optional)
const_id = 'const_id_example' # str | Filter by unique constituency identifier (uri) (optional)

try:
    # Members
    api_response = api_instance.members(date_start=date_start, chamber_id=chamber_id, chamber=chamber, house_no=house_no, member_id=member_id, date_end=date_end, skip=skip, limit=limit, party_code=party_code, party_id=party_id, const_code=const_code, const_id=const_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MembersApi->members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_start** | **date**| This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. | [optional] [default to 1900-01-01]
 **chamber_id** | [**list[str]**](str.md)| Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  | [optional] [default to []]
 **chamber** | **str**| Filter by House name (dail or seanad). Using an empty string retrieves results for both Houses.  | [optional] [default to ]
 **house_no** | **int**| filter by house number | [optional] 
 **member_id** | **str**| Filter by Member uri. | [optional] 
 **date_end** | **date**| This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. | [optional] [default to 2099-01-01]
 **skip** | **int**| This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. | [optional] [default to 0]
 **limit** | **int**| This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. | [optional] [default to 50]
 **party_code** | **str**| Filter by party code | [optional] 
 **party_id** | **str**| Filter by unique party identifier (uri) | [optional] 
 **const_code** | **str**| Filter by constituency code | [optional] 
 **const_id** | **str**| Filter by unique constituency identifier (uri) | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

