# openapi_client.AiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_list**](AiApi.md#ai_list) | **GET** /api/ai/ | 
[**ai_retrieve**](AiApi.md#ai_retrieve) | **GET** /api/ai/{id}/ | 
[**ai_update**](AiApi.md#ai_update) | **PUT** /api/ai/{id}/ | 


# **ai_list**
> List[ActionAI] ai_list(action_type__code=action_type__code, is_public=is_public, person=person, status=status)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.action_ai import ActionAI
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AiApi(api_client)
    action_type__code = 'action_type__code_example' # str |  (optional)
    is_public = True # bool |  (optional)
    person = 56 # int |  (optional)
    status = 'status_example' # str | * `hold` - نگه داشته شده * `pending` - در انتظار * `in_progress` - در حال انجام * `done` - انجام شده (optional)

    try:
        api_response = api_instance.ai_list(action_type__code=action_type__code, is_public=is_public, person=person, status=status)
        print("The response of AiApi->ai_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->ai_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type__code** | **str**|  | [optional] 
 **is_public** | **bool**|  | [optional] 
 **person** | **int**|  | [optional] 
 **status** | **str**| * &#x60;hold&#x60; - نگه داشته شده * &#x60;pending&#x60; - در انتظار * &#x60;in_progress&#x60; - در حال انجام * &#x60;done&#x60; - انجام شده | [optional] 

### Return type

[**List[ActionAI]**](ActionAI.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_retrieve**
> ActionAI ai_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.action_ai import ActionAI
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AiApi(api_client)
    id = 56 # int | A unique integer value identifying this action.

    try:
        api_response = api_instance.ai_retrieve(id)
        print("The response of AiApi->ai_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->ai_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this action. | 

### Return type

[**ActionAI**](ActionAI.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_update**
> ActionAI ai_update(id, action_ai=action_ai)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.action_ai import ActionAI
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AiApi(api_client)
    id = 56 # int | A unique integer value identifying this action.
    action_ai = openapi_client.ActionAI() # ActionAI |  (optional)

    try:
        api_response = api_instance.ai_update(id, action_ai=action_ai)
        print("The response of AiApi->ai_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AiApi->ai_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this action. | 
 **action_ai** | [**ActionAI**](ActionAI.md)|  | [optional] 

### Return type

[**ActionAI**](ActionAI.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

