# openapi_client.EmploymentHistoryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employment_history_create**](EmploymentHistoryApi.md#employment_history_create) | **POST** /api/employment_history/ | 
[**employment_history_destroy**](EmploymentHistoryApi.md#employment_history_destroy) | **DELETE** /api/employment_history/{id}/ | 
[**employment_history_list**](EmploymentHistoryApi.md#employment_history_list) | **GET** /api/employment_history/ | 
[**employment_history_partial_update**](EmploymentHistoryApi.md#employment_history_partial_update) | **PATCH** /api/employment_history/{id}/ | 
[**employment_history_retrieve**](EmploymentHistoryApi.md#employment_history_retrieve) | **GET** /api/employment_history/{id}/ | 
[**employment_history_update**](EmploymentHistoryApi.md#employment_history_update) | **PUT** /api/employment_history/{id}/ | 


# **employment_history_create**
> EmploymentHistory employment_history_create(employment_history)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.employment_history import EmploymentHistory
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
    api_instance = openapi_client.EmploymentHistoryApi(api_client)
    employment_history = openapi_client.EmploymentHistory() # EmploymentHistory | 

    try:
        api_response = api_instance.employment_history_create(employment_history)
        print("The response of EmploymentHistoryApi->employment_history_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentHistoryApi->employment_history_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employment_history** | [**EmploymentHistory**](EmploymentHistory.md)|  | 

### Return type

[**EmploymentHistory**](EmploymentHistory.md)

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

# **employment_history_destroy**
> employment_history_destroy(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
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
    api_instance = openapi_client.EmploymentHistoryApi(api_client)
    id = 56 # int | A unique integer value identifying this سابقه شغلی.

    try:
        api_instance.employment_history_destroy(id)
    except Exception as e:
        print("Exception when calling EmploymentHistoryApi->employment_history_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سابقه شغلی. | 

### Return type

void (empty response body)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employment_history_list**
> List[EmploymentHistory] employment_history_list(person=person)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.employment_history import EmploymentHistory
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
    api_instance = openapi_client.EmploymentHistoryApi(api_client)
    person = 56 # int |  (optional)

    try:
        api_response = api_instance.employment_history_list(person=person)
        print("The response of EmploymentHistoryApi->employment_history_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentHistoryApi->employment_history_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person** | **int**|  | [optional] 

### Return type

[**List[EmploymentHistory]**](EmploymentHistory.md)

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

# **employment_history_partial_update**
> EmploymentHistory employment_history_partial_update(id, patched_employment_history=patched_employment_history)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.employment_history import EmploymentHistory
from openapi_client.models.patched_employment_history import PatchedEmploymentHistory
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
    api_instance = openapi_client.EmploymentHistoryApi(api_client)
    id = 56 # int | A unique integer value identifying this سابقه شغلی.
    patched_employment_history = openapi_client.PatchedEmploymentHistory() # PatchedEmploymentHistory |  (optional)

    try:
        api_response = api_instance.employment_history_partial_update(id, patched_employment_history=patched_employment_history)
        print("The response of EmploymentHistoryApi->employment_history_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentHistoryApi->employment_history_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سابقه شغلی. | 
 **patched_employment_history** | [**PatchedEmploymentHistory**](PatchedEmploymentHistory.md)|  | [optional] 

### Return type

[**EmploymentHistory**](EmploymentHistory.md)

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

# **employment_history_retrieve**
> EmploymentHistory employment_history_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.employment_history import EmploymentHistory
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
    api_instance = openapi_client.EmploymentHistoryApi(api_client)
    id = 56 # int | A unique integer value identifying this سابقه شغلی.

    try:
        api_response = api_instance.employment_history_retrieve(id)
        print("The response of EmploymentHistoryApi->employment_history_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentHistoryApi->employment_history_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سابقه شغلی. | 

### Return type

[**EmploymentHistory**](EmploymentHistory.md)

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

# **employment_history_update**
> EmploymentHistory employment_history_update(id, employment_history)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.employment_history import EmploymentHistory
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
    api_instance = openapi_client.EmploymentHistoryApi(api_client)
    id = 56 # int | A unique integer value identifying this سابقه شغلی.
    employment_history = openapi_client.EmploymentHistory() # EmploymentHistory | 

    try:
        api_response = api_instance.employment_history_update(id, employment_history)
        print("The response of EmploymentHistoryApi->employment_history_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmploymentHistoryApi->employment_history_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سابقه شغلی. | 
 **employment_history** | [**EmploymentHistory**](EmploymentHistory.md)|  | 

### Return type

[**EmploymentHistory**](EmploymentHistory.md)

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

