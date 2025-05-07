# openapi_client.ObservationTypesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**observation_types_list**](ObservationTypesApi.md#observation_types_list) | **GET** /api/observation_types/ | 
[**observation_types_retrieve**](ObservationTypesApi.md#observation_types_retrieve) | **GET** /api/observation_types/{id}/ | 


# **observation_types_list**
> List[ObservationType] observation_types_list(category__code=category__code, code=code, examination_types__code=examination_types__code, sections__code=sections__code)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.observation_type import ObservationType
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
    api_instance = openapi_client.ObservationTypesApi(api_client)
    category__code = 'category__code_example' # str |  (optional)
    code = 'code_example' # str |  (optional)
    examination_types__code = 'examination_types__code_example' # str |  (optional)
    sections__code = ['sections__code_example'] # List[Optional[str]] | ممکن است چندین مقدار با کاما از هم جدا شوند. (optional)

    try:
        api_response = api_instance.observation_types_list(category__code=category__code, code=code, examination_types__code=examination_types__code, sections__code=sections__code)
        print("The response of ObservationTypesApi->observation_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationTypesApi->observation_types_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category__code** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **examination_types__code** | **str**|  | [optional] 
 **sections__code** | [**List[Optional[str]]**](str.md)| ممکن است چندین مقدار با کاما از هم جدا شوند. | [optional] 

### Return type

[**List[ObservationType]**](ObservationType.md)

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

# **observation_types_retrieve**
> ObservationType observation_types_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.observation_type import ObservationType
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
    api_instance = openapi_client.ObservationTypesApi(api_client)
    id = 56 # int | A unique integer value identifying this observation type.

    try:
        api_response = api_instance.observation_types_retrieve(id)
        print("The response of ObservationTypesApi->observation_types_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ObservationTypesApi->observation_types_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this observation type. | 

### Return type

[**ObservationType**](ObservationType.md)

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

