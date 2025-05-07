# openapi_client.ExaminationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**examinations_create**](ExaminationsApi.md#examinations_create) | **POST** /api/examinations/ | 
[**examinations_destroy**](ExaminationsApi.md#examinations_destroy) | **DELETE** /api/examinations/{id}/ | 
[**examinations_list**](ExaminationsApi.md#examinations_list) | **GET** /api/examinations/ | 
[**examinations_partial_update**](ExaminationsApi.md#examinations_partial_update) | **PATCH** /api/examinations/{id}/ | 
[**examinations_retrieve**](ExaminationsApi.md#examinations_retrieve) | **GET** /api/examinations/{id}/ | 
[**examinations_update**](ExaminationsApi.md#examinations_update) | **PUT** /api/examinations/{id}/ | 


# **examinations_create**
> Examination examinations_create(examination)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.examination import Examination
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
    api_instance = openapi_client.ExaminationsApi(api_client)
    examination = openapi_client.Examination() # Examination | 

    try:
        api_response = api_instance.examinations_create(examination)
        print("The response of ExaminationsApi->examinations_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExaminationsApi->examinations_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **examination** | [**Examination**](Examination.md)|  | 

### Return type

[**Examination**](Examination.md)

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

# **examinations_destroy**
> examinations_destroy(id)

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
    api_instance = openapi_client.ExaminationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.

    try:
        api_instance.examinations_destroy(id)
    except Exception as e:
        print("Exception when calling ExaminationsApi->examinations_destroy: %s\n" % e)
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

# **examinations_list**
> List[Examination] examinations_list(employment_history=employment_history, examination_type__code=examination_type__code, person=person)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.examination import Examination
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
    api_instance = openapi_client.ExaminationsApi(api_client)
    employment_history = 'employment_history_example' # str |  (optional)
    examination_type__code = ['examination_type__code_example'] # List[Optional[str]] | ممکن است چندین مقدار با کاما از هم جدا شوند. (optional)
    person = 56 # int |  (optional)

    try:
        api_response = api_instance.examinations_list(employment_history=employment_history, examination_type__code=examination_type__code, person=person)
        print("The response of ExaminationsApi->examinations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExaminationsApi->examinations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employment_history** | **str**|  | [optional] 
 **examination_type__code** | [**List[Optional[str]]**](str.md)| ممکن است چندین مقدار با کاما از هم جدا شوند. | [optional] 
 **person** | **int**|  | [optional] 

### Return type

[**List[Examination]**](Examination.md)

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

# **examinations_partial_update**
> Examination examinations_partial_update(id, patched_examination=patched_examination)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.examination import Examination
from openapi_client.models.patched_examination import PatchedExamination
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
    api_instance = openapi_client.ExaminationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.
    patched_examination = openapi_client.PatchedExamination() # PatchedExamination |  (optional)

    try:
        api_response = api_instance.examinations_partial_update(id, patched_examination=patched_examination)
        print("The response of ExaminationsApi->examinations_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExaminationsApi->examinations_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 
 **patched_examination** | [**PatchedExamination**](PatchedExamination.md)|  | [optional] 

### Return type

[**Examination**](Examination.md)

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

# **examinations_retrieve**
> Examination examinations_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.examination import Examination
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
    api_instance = openapi_client.ExaminationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.

    try:
        api_response = api_instance.examinations_retrieve(id)
        print("The response of ExaminationsApi->examinations_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExaminationsApi->examinations_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 

### Return type

[**Examination**](Examination.md)

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

# **examinations_update**
> Examination examinations_update(id, examination)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.examination import Examination
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
    api_instance = openapi_client.ExaminationsApi(api_client)
    id = 56 # int | A unique integer value identifying this examination.
    examination = openapi_client.Examination() # Examination | 

    try:
        api_response = api_instance.examinations_update(id, examination)
        print("The response of ExaminationsApi->examinations_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExaminationsApi->examinations_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this examination. | 
 **examination** | [**Examination**](Examination.md)|  | 

### Return type

[**Examination**](Examination.md)

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

