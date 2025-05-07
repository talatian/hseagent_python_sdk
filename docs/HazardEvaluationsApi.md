# hseagent_sdk.HazardEvaluationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hazard_evaluations_create**](HazardEvaluationsApi.md#hazard_evaluations_create) | **POST** /api/hazard_evaluations/ | 
[**hazard_evaluations_destroy**](HazardEvaluationsApi.md#hazard_evaluations_destroy) | **DELETE** /api/hazard_evaluations/{id}/ | 
[**hazard_evaluations_list**](HazardEvaluationsApi.md#hazard_evaluations_list) | **GET** /api/hazard_evaluations/ | 
[**hazard_evaluations_partial_update**](HazardEvaluationsApi.md#hazard_evaluations_partial_update) | **PATCH** /api/hazard_evaluations/{id}/ | 
[**hazard_evaluations_retrieve**](HazardEvaluationsApi.md#hazard_evaluations_retrieve) | **GET** /api/hazard_evaluations/{id}/ | 
[**hazard_evaluations_update**](HazardEvaluationsApi.md#hazard_evaluations_update) | **PUT** /api/hazard_evaluations/{id}/ | 


# **hazard_evaluations_create**
> HazardEvaluation hazard_evaluations_create(hazard_evaluation)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.hazard_evaluation import HazardEvaluation
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
    api_instance = hseagent_sdk.HazardEvaluationsApi(api_client)
    hazard_evaluation = hseagent_sdk.HazardEvaluation() # HazardEvaluation | 

    try:
        api_response = api_instance.hazard_evaluations_create(hazard_evaluation)
        print("The response of HazardEvaluationsApi->hazard_evaluations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HazardEvaluationsApi->hazard_evaluations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hazard_evaluation** | [**HazardEvaluation**](HazardEvaluation.md)|  | 

### Return type

[**HazardEvaluation**](HazardEvaluation.md)

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

# **hazard_evaluations_destroy**
> hazard_evaluations_destroy(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
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
    api_instance = hseagent_sdk.HazardEvaluationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.

    try:
        api_instance.hazard_evaluations_destroy(id)
    except Exception as e:
        print("Exception when calling HazardEvaluationsApi->hazard_evaluations_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 

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

# **hazard_evaluations_list**
> List[HazardEvaluation] hazard_evaluations_list(employment_history=employment_history, examination_type__code=examination_type__code, person=person)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.hazard_evaluation import HazardEvaluation
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
    api_instance = hseagent_sdk.HazardEvaluationsApi(api_client)
    employment_history = 'employment_history_example' # str |  (optional)
    examination_type__code = ['examination_type__code_example'] # List[Optional[str]] | ممکن است چندین مقدار با کاما از هم جدا شوند. (optional)
    person = 56 # int |  (optional)

    try:
        api_response = api_instance.hazard_evaluations_list(employment_history=employment_history, examination_type__code=examination_type__code, person=person)
        print("The response of HazardEvaluationsApi->hazard_evaluations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HazardEvaluationsApi->hazard_evaluations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employment_history** | **str**|  | [optional] 
 **examination_type__code** | [**List[Optional[str]]**](str.md)| ممکن است چندین مقدار با کاما از هم جدا شوند. | [optional] 
 **person** | **int**|  | [optional] 

### Return type

[**List[HazardEvaluation]**](HazardEvaluation.md)

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

# **hazard_evaluations_partial_update**
> HazardEvaluation hazard_evaluations_partial_update(id, patched_hazard_evaluation=patched_hazard_evaluation)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.hazard_evaluation import HazardEvaluation
from hseagent_sdk.models.patched_hazard_evaluation import PatchedHazardEvaluation
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
    api_instance = hseagent_sdk.HazardEvaluationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.
    patched_hazard_evaluation = hseagent_sdk.PatchedHazardEvaluation() # PatchedHazardEvaluation |  (optional)

    try:
        api_response = api_instance.hazard_evaluations_partial_update(id, patched_hazard_evaluation=patched_hazard_evaluation)
        print("The response of HazardEvaluationsApi->hazard_evaluations_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HazardEvaluationsApi->hazard_evaluations_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 
 **patched_hazard_evaluation** | [**PatchedHazardEvaluation**](PatchedHazardEvaluation.md)|  | [optional] 

### Return type

[**HazardEvaluation**](HazardEvaluation.md)

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

# **hazard_evaluations_retrieve**
> HazardEvaluation hazard_evaluations_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.hazard_evaluation import HazardEvaluation
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
    api_instance = hseagent_sdk.HazardEvaluationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.

    try:
        api_response = api_instance.hazard_evaluations_retrieve(id)
        print("The response of HazardEvaluationsApi->hazard_evaluations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HazardEvaluationsApi->hazard_evaluations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 

### Return type

[**HazardEvaluation**](HazardEvaluation.md)

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

# **hazard_evaluations_update**
> HazardEvaluation hazard_evaluations_update(id, hazard_evaluation)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.hazard_evaluation import HazardEvaluation
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
    api_instance = hseagent_sdk.HazardEvaluationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.
    hazard_evaluation = hseagent_sdk.HazardEvaluation() # HazardEvaluation | 

    try:
        api_response = api_instance.hazard_evaluations_update(id, hazard_evaluation)
        print("The response of HazardEvaluationsApi->hazard_evaluations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HazardEvaluationsApi->hazard_evaluations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 
 **hazard_evaluation** | [**HazardEvaluation**](HazardEvaluation.md)|  | 

### Return type

[**HazardEvaluation**](HazardEvaluation.md)

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

