# hseagent_sdk.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roles_create**](RolesApi.md#roles_create) | **POST** /api/roles/ | 
[**roles_destroy**](RolesApi.md#roles_destroy) | **DELETE** /api/roles/{id}/ | 
[**roles_list**](RolesApi.md#roles_list) | **GET** /api/roles/ | 
[**roles_partial_update**](RolesApi.md#roles_partial_update) | **PATCH** /api/roles/{id}/ | 
[**roles_retrieve**](RolesApi.md#roles_retrieve) | **GET** /api/roles/{id}/ | 
[**roles_update**](RolesApi.md#roles_update) | **PUT** /api/roles/{id}/ | 


# **roles_create**
> Role roles_create(role)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.role import Role
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
    api_instance = hseagent_sdk.RolesApi(api_client)
    role = hseagent_sdk.Role() # Role | 

    try:
        api_response = api_instance.roles_create(role)
        print("The response of RolesApi->roles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

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

# **roles_destroy**
> roles_destroy(id)

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
    api_instance = hseagent_sdk.RolesApi(api_client)
    id = 56 # int | A unique integer value identifying this سمت.

    try:
        api_instance.roles_destroy(id)
    except Exception as e:
        print("Exception when calling RolesApi->roles_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سمت. | 

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

# **roles_list**
> List[Role] roles_list()

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.role import Role
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
    api_instance = hseagent_sdk.RolesApi(api_client)

    try:
        api_response = api_instance.roles_list()
        print("The response of RolesApi->roles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Role]**](Role.md)

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

# **roles_partial_update**
> Role roles_partial_update(id, patched_role=patched_role)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.patched_role import PatchedRole
from hseagent_sdk.models.role import Role
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
    api_instance = hseagent_sdk.RolesApi(api_client)
    id = 56 # int | A unique integer value identifying this سمت.
    patched_role = hseagent_sdk.PatchedRole() # PatchedRole |  (optional)

    try:
        api_response = api_instance.roles_partial_update(id, patched_role=patched_role)
        print("The response of RolesApi->roles_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سمت. | 
 **patched_role** | [**PatchedRole**](PatchedRole.md)|  | [optional] 

### Return type

[**Role**](Role.md)

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

# **roles_retrieve**
> Role roles_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.role import Role
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
    api_instance = hseagent_sdk.RolesApi(api_client)
    id = 56 # int | A unique integer value identifying this سمت.

    try:
        api_response = api_instance.roles_retrieve(id)
        print("The response of RolesApi->roles_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سمت. | 

### Return type

[**Role**](Role.md)

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

# **roles_update**
> Role roles_update(id, role)

### Example

* Api Key Authentication (tokenAuth):

```python
import hseagent_sdk
from hseagent_sdk.models.role import Role
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
    api_instance = hseagent_sdk.RolesApi(api_client)
    id = 56 # int | A unique integer value identifying this سمت.
    role = hseagent_sdk.Role() # Role | 

    try:
        api_response = api_instance.roles_update(id, role)
        print("The response of RolesApi->roles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->roles_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this سمت. | 
 **role** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

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

