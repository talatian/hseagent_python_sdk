# openapi_client.DepartmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**departments_create**](DepartmentsApi.md#departments_create) | **POST** /api/departments/ | 
[**departments_destroy**](DepartmentsApi.md#departments_destroy) | **DELETE** /api/departments/{id}/ | 
[**departments_list**](DepartmentsApi.md#departments_list) | **GET** /api/departments/ | 
[**departments_partial_update**](DepartmentsApi.md#departments_partial_update) | **PATCH** /api/departments/{id}/ | 
[**departments_retrieve**](DepartmentsApi.md#departments_retrieve) | **GET** /api/departments/{id}/ | 
[**departments_update**](DepartmentsApi.md#departments_update) | **PUT** /api/departments/{id}/ | 


# **departments_create**
> Department departments_create(department)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.department import Department
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    department = openapi_client.Department() # Department | 

    try:
        api_response = api_instance.departments_create(department)
        print("The response of DepartmentsApi->departments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->departments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department** | [**Department**](Department.md)|  | 

### Return type

[**Department**](Department.md)

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

# **departments_destroy**
> departments_destroy(id)

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
    api_instance = openapi_client.DepartmentsApi(api_client)
    id = 56 # int | A unique integer value identifying this دپارتمان.

    try:
        api_instance.departments_destroy(id)
    except Exception as e:
        print("Exception when calling DepartmentsApi->departments_destroy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this دپارتمان. | 

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

# **departments_list**
> List[Department] departments_list()

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.department import Department
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
    api_instance = openapi_client.DepartmentsApi(api_client)

    try:
        api_response = api_instance.departments_list()
        print("The response of DepartmentsApi->departments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->departments_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Department]**](Department.md)

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

# **departments_partial_update**
> Department departments_partial_update(id, patched_department=patched_department)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.department import Department
from openapi_client.models.patched_department import PatchedDepartment
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    id = 56 # int | A unique integer value identifying this دپارتمان.
    patched_department = openapi_client.PatchedDepartment() # PatchedDepartment |  (optional)

    try:
        api_response = api_instance.departments_partial_update(id, patched_department=patched_department)
        print("The response of DepartmentsApi->departments_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->departments_partial_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this دپارتمان. | 
 **patched_department** | [**PatchedDepartment**](PatchedDepartment.md)|  | [optional] 

### Return type

[**Department**](Department.md)

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

# **departments_retrieve**
> Department departments_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.department import Department
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    id = 56 # int | A unique integer value identifying this دپارتمان.

    try:
        api_response = api_instance.departments_retrieve(id)
        print("The response of DepartmentsApi->departments_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->departments_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this دپارتمان. | 

### Return type

[**Department**](Department.md)

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

# **departments_update**
> Department departments_update(id, department)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.department import Department
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
    api_instance = openapi_client.DepartmentsApi(api_client)
    id = 56 # int | A unique integer value identifying this دپارتمان.
    department = openapi_client.Department() # Department | 

    try:
        api_response = api_instance.departments_update(id, department)
        print("The response of DepartmentsApi->departments_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DepartmentsApi->departments_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this دپارتمان. | 
 **department** | [**Department**](Department.md)|  | 

### Return type

[**Department**](Department.md)

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

