# openapi_client.PhysiciansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**physicians_create**](PhysiciansApi.md#physicians_create) | **POST** /api/physicians/ | 
[**physicians_destroy**](PhysiciansApi.md#physicians_destroy) | **DELETE** /api/physicians/{id}/ | 
[**physicians_list**](PhysiciansApi.md#physicians_list) | **GET** /api/physicians/ | 
[**physicians_partial_update**](PhysiciansApi.md#physicians_partial_update) | **PATCH** /api/physicians/{id}/ | 
[**physicians_retrieve**](PhysiciansApi.md#physicians_retrieve) | **GET** /api/physicians/{id}/ | 
[**physicians_update**](PhysiciansApi.md#physicians_update) | **PUT** /api/physicians/{id}/ | 


# **physicians_create**
> Physician physicians_create(physician)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.physician import Physician
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
    api_instance = openapi_client.PhysiciansApi(api_client)
    physician = openapi_client.Physician() # Physician | 

    try:
        api_response = api_instance.physicians_create(physician)
        print("The response of PhysiciansApi->physicians_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhysiciansApi->physicians_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physician** | [**Physician**](Physician.md)|  | 

### Return type

[**Physician**](Physician.md)

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

# **physicians_destroy**
> physicians_destroy(id)

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
    api_instance = openapi_client.PhysiciansApi(api_client)
    id = 56 # int | A unique integer value identifying this پزشک.

    try:
        api_instance.physicians_destroy(id)
    except Exception as e:
        print("Exception when calling PhysiciansApi->physicians_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this پزشک. | 

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

# **physicians_list**
> List[Physician] physicians_list(is_active=is_active)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.physician import Physician
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
    api_instance = openapi_client.PhysiciansApi(api_client)
    is_active = True # bool |  (optional)

    try:
        api_response = api_instance.physicians_list(is_active=is_active)
        print("The response of PhysiciansApi->physicians_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhysiciansApi->physicians_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_active** | **bool**|  | [optional] 

### Return type

[**List[Physician]**](Physician.md)

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

# **physicians_partial_update**
> Physician physicians_partial_update(id, patched_physician=patched_physician)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.patched_physician import PatchedPhysician
from openapi_client.models.physician import Physician
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
    api_instance = openapi_client.PhysiciansApi(api_client)
    id = 56 # int | A unique integer value identifying this پزشک.
    patched_physician = openapi_client.PatchedPhysician() # PatchedPhysician |  (optional)

    try:
        api_response = api_instance.physicians_partial_update(id, patched_physician=patched_physician)
        print("The response of PhysiciansApi->physicians_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhysiciansApi->physicians_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this پزشک. | 
 **patched_physician** | [**PatchedPhysician**](PatchedPhysician.md)|  | [optional] 

### Return type

[**Physician**](Physician.md)

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

# **physicians_retrieve**
> Physician physicians_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.physician import Physician
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
    api_instance = openapi_client.PhysiciansApi(api_client)
    id = 56 # int | A unique integer value identifying this پزشک.

    try:
        api_response = api_instance.physicians_retrieve(id)
        print("The response of PhysiciansApi->physicians_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhysiciansApi->physicians_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this پزشک. | 

### Return type

[**Physician**](Physician.md)

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

# **physicians_update**
> Physician physicians_update(id, physician)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.physician import Physician
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
    api_instance = openapi_client.PhysiciansApi(api_client)
    id = 56 # int | A unique integer value identifying this پزشک.
    physician = openapi_client.Physician() # Physician | 

    try:
        api_response = api_instance.physicians_update(id, physician)
        print("The response of PhysiciansApi->physicians_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhysiciansApi->physicians_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this پزشک. | 
 **physician** | [**Physician**](Physician.md)|  | 

### Return type

[**Physician**](Physician.md)

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

