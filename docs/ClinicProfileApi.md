# hseagent_sdk.ClinicProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clinic_profile_partial_update**](ClinicProfileApi.md#clinic_profile_partial_update) | **PATCH** /api/clinic-profile | 
[**clinic_profile_retrieve**](ClinicProfileApi.md#clinic_profile_retrieve) | **GET** /api/clinic-profile | 
[**clinic_profile_update**](ClinicProfileApi.md#clinic_profile_update) | **PUT** /api/clinic-profile | 


# **clinic_profile_partial_update**
> ClinicProfile clinic_profile_partial_update(patched_clinic_profile=patched_clinic_profile)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.clinic_profile import ClinicProfile
from hseagent_sdk.models.patched_clinic_profile import PatchedClinicProfile
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
    api_instance = hseagent_sdk.ClinicProfileApi(api_client)
    patched_clinic_profile = hseagent_sdk.PatchedClinicProfile() # PatchedClinicProfile |  (optional)

    try:
        api_response = api_instance.clinic_profile_partial_update(patched_clinic_profile=patched_clinic_profile)
        print("The response of ClinicProfileApi->clinic_profile_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClinicProfileApi->clinic_profile_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patched_clinic_profile** | [**PatchedClinicProfile**](PatchedClinicProfile.md)|  | [optional] 

### Return type

[**ClinicProfile**](ClinicProfile.md)

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

# **clinic_profile_retrieve**
> ClinicProfile clinic_profile_retrieve()

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.clinic_profile import ClinicProfile
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
    api_instance = hseagent_sdk.ClinicProfileApi(api_client)

    try:
        api_response = api_instance.clinic_profile_retrieve()
        print("The response of ClinicProfileApi->clinic_profile_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClinicProfileApi->clinic_profile_retrieve: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClinicProfile**](ClinicProfile.md)

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

# **clinic_profile_update**
> ClinicProfile clinic_profile_update(clinic_profile)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.clinic_profile import ClinicProfile
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
    api_instance = hseagent_sdk.ClinicProfileApi(api_client)
    clinic_profile = hseagent_sdk.ClinicProfile() # ClinicProfile | 

    try:
        api_response = api_instance.clinic_profile_update(clinic_profile)
        print("The response of ClinicProfileApi->clinic_profile_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClinicProfileApi->clinic_profile_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clinic_profile** | [**ClinicProfile**](ClinicProfile.md)|  | 

### Return type

[**ClinicProfile**](ClinicProfile.md)

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

