# openapi_client.HseProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**hse_profile_partial_update**](HseProfileApi.md#hse_profile_partial_update) | **PATCH** /api/hse-profile | 
[**hse_profile_retrieve**](HseProfileApi.md#hse_profile_retrieve) | **GET** /api/hse-profile | 
[**hse_profile_update**](HseProfileApi.md#hse_profile_update) | **PUT** /api/hse-profile | 


# **hse_profile_partial_update**
> HSEProfile hse_profile_partial_update(patched_hse_profile=patched_hse_profile)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.hse_profile import HSEProfile
from openapi_client.models.patched_hse_profile import PatchedHSEProfile
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
    api_instance = openapi_client.HseProfileApi(api_client)
    patched_hse_profile = openapi_client.PatchedHSEProfile() # PatchedHSEProfile |  (optional)

    try:
        api_response = api_instance.hse_profile_partial_update(patched_hse_profile=patched_hse_profile)
        print("The response of HseProfileApi->hse_profile_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HseProfileApi->hse_profile_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_hse_profile** | [**PatchedHSEProfile**](PatchedHSEProfile.md)|  | [optional] 

### Return type

[**HSEProfile**](HSEProfile.md)

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

# **hse_profile_retrieve**
> HSEProfile hse_profile_retrieve()

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.hse_profile import HSEProfile
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
    api_instance = openapi_client.HseProfileApi(api_client)

    try:
        api_response = api_instance.hse_profile_retrieve()
        print("The response of HseProfileApi->hse_profile_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HseProfileApi->hse_profile_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HSEProfile**](HSEProfile.md)

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

# **hse_profile_update**
> HSEProfile hse_profile_update(hse_profile)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.hse_profile import HSEProfile
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
    api_instance = openapi_client.HseProfileApi(api_client)
    hse_profile = openapi_client.HSEProfile() # HSEProfile | 

    try:
        api_response = api_instance.hse_profile_update(hse_profile)
        print("The response of HseProfileApi->hse_profile_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HseProfileApi->hse_profile_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hse_profile** | [**HSEProfile**](HSEProfile.md)|  | 

### Return type

[**HSEProfile**](HSEProfile.md)

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

