# oireachtas_api.QuestionsApi

All URIs are relative to *https://api.oireachtas.ie/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**questions**](QuestionsApi.md#questions) | **GET** /questions | Questions Filtered by Type Only


# **questions**
> InlineResponse2001 questions(date_start=date_start, date_end=date_end, skip=skip, limit=limit, qtype=qtype, member_id=member_id, question_id=question_id, question_no=question_no)

Questions Filtered by Type Only

Returns list of questions filtered by the base and additional parameters. The list supports paging. #### Mapping * Start Date - Greater Than or Equal To - question.date * End Date - Less Than or Equal To - question.date * Skip - Equal To - this will ignore the first x number of records set in the parameter * Limit - Equal To - this will only return a specific amount of records * Question Type - question.questionType 

### Example
```python
from __future__ import print_function
import time
import oireachtas_api
from oireachtas_api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = oireachtas_api.QuestionsApi()
date_start = '1900-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. (optional) (default to 1900-01-01)
date_end = '2099-01-01' # date | This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. (optional) (default to 2099-01-01)
skip = 0 # int | This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. (optional) (default to 0)
limit = 50 # int | This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. (optional) (default to 50)
qtype = ['[\"oral\",\"written\"]'] # list[str] | Filter questions by oral or writtens. (optional) (default to ["oral","written"])
member_id = 'member_id_example' # str | Filter by Member uri. (optional)
question_id = 'question_id_example' # str | Identifier for a Single Question (optional)
question_no = 56 # int | Filter by question No. (optional)

try:
    # Questions Filtered by Type Only
    api_response = api_instance.questions(date_start=date_start, date_end=date_end, skip=skip, limit=limit, qtype=qtype, member_id=member_id, question_id=question_id, question_no=question_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuestionsApi->questions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_start** | **date**| This is a base filter which is used on many APIs, allowing filtering by Start Date related to the Section. | [optional] [default to 1900-01-01]
 **date_end** | **date**| This is a base filter which is used on many APIs, allowing filtering by End Date related to the Section. | [optional] [default to 2099-01-01]
 **skip** | **int**| This is a base filter which is used on many APIs, allowing skipping of records by a specific integer. | [optional] [default to 0]
 **limit** | **int**| This is a base filter which is used on many APIs, allowing the limiting of records to a specific integer. | [optional] [default to 50]
 **qtype** | [**list[str]**](str.md)| Filter questions by oral or writtens. | [optional] [default to [&quot;oral&quot;,&quot;written&quot;]]
 **member_id** | **str**| Filter by Member uri. | [optional] 
 **question_id** | **str**| Identifier for a Single Question | [optional] 
 **question_no** | **int**| Filter by question No. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

