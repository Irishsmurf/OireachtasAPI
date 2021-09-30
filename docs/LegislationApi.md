# oireachtas_api.LegislationApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**legislation**](LegislationApi.md#legislation) | **GET** /legislation | Legislation API


# **legislation**
> InlineResponse200 legislation(bill_status=bill_status, bill_source=bill_source, date_start=date_start, date_end=date_end, skip=skip, limit=limit, member_id=member_id, bill_id=bill_id, bill_no=bill_no, bill_year=bill_year, chamber_id=chamber_id, act_year=act_year, act_no=act_no, lang=lang)

Legislation API

Returns list of bills filtered by the base and additional parameters. The list supports paging. #### Indexes * billsbook_meta  #### Mapping * Start Date - Greater Than or Equal To - bill.mostRecentStage.event.dates.date * End Date - Less Than or Equal To - bill.mostRecentStage.event.dates.date * Skip - Equal To - this will ignore the first x number of records set in the parameter * Limit - Equal To - this will only return a specific amount of records * Status - Equal To - bill.status * Source - Equal To - bill.source * 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.LegislationApi()
bill_status = ['[\"Current\",\"Withdrawn\",\"Enacted\",\"Rejected\",\"Defeated\",\"Lapsed\"]'] # list[str] | An array which is used to filter legislation by status detailed in default settings below.  Separated by comma. (optional) (default to ["Current","Withdrawn","Enacted","Rejected","Defeated","Lapsed"])
bill_source = ['[\"Government\",\"Private Member\"]'] # list[str] | An array used to filter legislation by origin source. (optional) (default to ["Government","Private Member"])
date_start = '1900-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
date_end = '2099-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
member_id = 'member_id_example' # str | Filter by Member uri. (optional)
bill_id = 'bill_id_example' # str | Filter results by Bill URI Example   /ie/oireachtas/bill/2016/2  (optional)
bill_no = 'bill_no_example' # str | Filter Bill by number. (optional)
bill_year = 'bill_year_example' # str | Filter Bill by year. (optional)
chamber_id = ['[]'] # list[str] | Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  (optional) (default to [])
act_year = 'act_year_example' # str | Filter Bill by Act year. (optional)
act_no = 'act_no_example' # str | Filter Bill by Act number. (optional)
lang = 'en' # str | language of document to extract. Defaults to English (en) (optional) (default to en)

try:
    # Legislation API
    api_response = api_instance.legislation(bill_status=bill_status, bill_source=bill_source, date_start=date_start, date_end=date_end, skip=skip, limit=limit, member_id=member_id, bill_id=bill_id, bill_no=bill_no, bill_year=bill_year, chamber_id=chamber_id, act_year=act_year, act_no=act_no, lang=lang)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LegislationApi->legislation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bill_status** | [**list[str]**](str.md)| An array which is used to filter legislation by status detailed in default settings below.  Separated by comma. | [optional] [default to [&quot;Current&quot;,&quot;Withdrawn&quot;,&quot;Enacted&quot;,&quot;Rejected&quot;,&quot;Defeated&quot;,&quot;Lapsed&quot;]]
 **bill_source** | [**list[str]**](str.md)| An array used to filter legislation by origin source. | [optional] [default to [&quot;Government&quot;,&quot;Private Member&quot;]]
 **date_start** | **date**| This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. | [optional] [default to 1900-01-01]
 **date_end** | **date**| This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. | [optional] [default to 2099-01-01]
 **skip** | **int**| This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. | [optional] [default to 0]
 **limit** | **int**| This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. | [optional] [default to 50]
 **member_id** | **str**| Filter by Member uri. | [optional] 
 **bill_id** | **str**| Filter results by Bill URI Example   /ie/oireachtas/bill/2016/2  | [optional] 
 **bill_no** | **str**| Filter Bill by number. | [optional] 
 **bill_year** | **str**| Filter Bill by year. | [optional] 
 **chamber_id** | [**list[str]**](str.md)| Filter by house or committee uri. Example  /ie/oireachtas/house/dail/32  | [optional] [default to []]
 **act_year** | **str**| Filter Bill by Act year. | [optional] 
 **act_no** | **str**| Filter Bill by Act number. | [optional] 
 **lang** | **str**| language of document to extract. Defaults to English (en) | [optional] [default to en]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

