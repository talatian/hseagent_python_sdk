# openapi_client.SectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sections_list**](SectionsApi.md#sections_list) | **GET** /api/sections/ | 
[**sections_retrieve**](SectionsApi.md#sections_retrieve) | **GET** /api/sections/{id}/ | 


# **sections_list**
> List[Section] sections_list(code=code, examination_type__code=examination_type__code, name=name, section_type__code=section_type__code)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.section import Section
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
    api_instance = openapi_client.SectionsApi(api_client)
    code = 'code_example' # str |  (optional)
    examination_type__code = 'examination_type__code_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    section_type__code = 'section_type__code_example' # str |  (optional)

    try:
        api_response = api_instance.sections_list(code=code, examination_type__code=examination_type__code, name=name, section_type__code=section_type__code)
        print("The response of SectionsApi->sections_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | [optional] 
 **examination_type__code** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **section_type__code** | **str**|  | [optional] 

### Return type

[**List[Section]**](Section.md)

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

# **sections_retrieve**
> Section sections_retrieve(id)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.section import Section
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
    api_instance = openapi_client.SectionsApi(api_client)
    id = 56 # int | A unique integer value identifying this section.

    try:
        api_response = api_instance.sections_retrieve(id)
        print("The response of SectionsApi->sections_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->sections_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this section. | 

### Return type

[**Section**](Section.md)

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

