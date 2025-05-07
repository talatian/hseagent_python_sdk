# hseagent_sdk.ActionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actions_create**](ActionsApi.md#actions_create) | **POST** /api/actions/ | 
[**actions_list**](ActionsApi.md#actions_list) | **GET** /api/actions/ | 
[**actions_retrieve**](ActionsApi.md#actions_retrieve) | **GET** /api/actions/{id}/ | 


# **actions_create**
> Action actions_create(action=action)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.action import Action
from hseagent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hseagent_sdk.Configuration(
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
with hseagent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hseagent_sdk.ActionsApi(api_client)
    action = hseagent_sdk.Action() # Action |  (optional)

    try:
        api_response = api_instance.actions_create(action=action)
        print("The response of ActionsApi->actions_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | [**Action**](Action.md)|  | [optional] 

### Return type

[**Action**](Action.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **actions_list**
> List[Action] actions_list(action_type__code=action_type__code, based_on_examination=based_on_examination, based_on_report=based_on_report, is_public=is_public, person=person, status=status)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.action import Action
from hseagent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hseagent_sdk.Configuration(
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
with hseagent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hseagent_sdk.ActionsApi(api_client)
    action_type__code = 'action_type__code_example' # str |  (optional)
    based_on_examination = 56 # int |  (optional)
    based_on_report = 56 # int |  (optional)
    is_public = True # bool |  (optional)
    person = 56 # int |  (optional)
    status = 'status_example' # str | * `hold` - نگه داشته شده * `pending` - در انتظار * `in_progress` - در حال انجام * `done` - انجام شده (optional)

    try:
        api_response = api_instance.actions_list(action_type__code=action_type__code, based_on_examination=based_on_examination, based_on_report=based_on_report, is_public=is_public, person=person, status=status)
        print("The response of ActionsApi->actions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type__code** | **str**|  | [optional] 
 **based_on_examination** | **int**|  | [optional] 
 **based_on_report** | **int**|  | [optional] 
 **is_public** | **bool**|  | [optional] 
 **person** | **int**|  | [optional] 
 **status** | **str**| * &#x60;hold&#x60; - نگه داشته شده * &#x60;pending&#x60; - در انتظار * &#x60;in_progress&#x60; - در حال انجام * &#x60;done&#x60; - انجام شده | [optional] 

### Return type

[**List[Action]**](Action.md)

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

# **actions_retrieve**
> Action actions_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.action import Action
from hseagent_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = hseagent_sdk.Configuration(
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
with hseagent_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = hseagent_sdk.ActionsApi(api_client)
    id = 56 # int | A unique integer value identifying this action.

    try:
        api_response = api_instance.actions_retrieve(id)
        print("The response of ActionsApi->actions_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->actions_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this action. | 

### Return type

[**Action**](Action.md)

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

