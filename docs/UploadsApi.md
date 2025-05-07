# openapi_client.UploadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**uploads_create**](UploadsApi.md#uploads_create) | **POST** /api/uploads/ | 


# **uploads_create**
> ObservationFile uploads_create(observation_file)

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.observation_file import ObservationFile
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
    api_instance = openapi_client.UploadsApi(api_client)
    observation_file = openapi_client.ObservationFile() # ObservationFile | 

    try:
        api_response = api_instance.uploads_create(observation_file)
        print("The response of UploadsApi->uploads_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadsApi->uploads_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **observation_file** | [**ObservationFile**](ObservationFile.md)|  | 

### Return type

[**ObservationFile**](ObservationFile.md)

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

