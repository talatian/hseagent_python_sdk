# openapi_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_email_create**](AuthApi.md#auth_email_create) | **POST** /api/auth/email/ | 
[**auth_mobile_create**](AuthApi.md#auth_mobile_create) | **POST** /api/auth/mobile/ | 
[**auth_token_create**](AuthApi.md#auth_token_create) | **POST** /api/auth/token/ | 
[**auth_verify_create**](AuthApi.md#auth_verify_create) | **POST** /api/auth/verify/ | 
[**auth_verify_email_create**](AuthApi.md#auth_verify_email_create) | **POST** /api/auth/verify/email/ | 
[**auth_verify_mobile_create**](AuthApi.md#auth_verify_mobile_create) | **POST** /api/auth/verify/mobile/ | 


# **auth_email_create**
> EmailAuth auth_email_create(email_auth)

This returns a 6-digit callback token we can trade for a user's Auth Token.

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.email_auth import EmailAuth
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
    api_instance = openapi_client.AuthApi(api_client)
    email_auth = openapi_client.EmailAuth() # EmailAuth | 

    try:
        api_response = api_instance.auth_email_create(email_auth)
        print("The response of AuthApi->auth_email_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_email_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_auth** | [**EmailAuth**](EmailAuth.md)|  | 

### Return type

[**EmailAuth**](EmailAuth.md)

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

# **auth_mobile_create**
> MobileAuth auth_mobile_create(mobile_auth)

This returns a 6-digit callback token we can trade for a user's Auth Token.

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.mobile_auth import MobileAuth
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
    api_instance = openapi_client.AuthApi(api_client)
    mobile_auth = openapi_client.MobileAuth() # MobileAuth | 

    try:
        api_response = api_instance.auth_mobile_create(mobile_auth)
        print("The response of AuthApi->auth_mobile_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_mobile_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_auth** | [**MobileAuth**](MobileAuth.md)|  | 

### Return type

[**MobileAuth**](MobileAuth.md)

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

# **auth_token_create**
> CallbackTokenAuth auth_token_create(callback_token_auth)

This is a duplicate of rest_framework's own ObtainAuthToken method.
Instead, this returns an Auth Token based on our callback token and source.

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.callback_token_auth import CallbackTokenAuth
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
    api_instance = openapi_client.AuthApi(api_client)
    callback_token_auth = openapi_client.CallbackTokenAuth() # CallbackTokenAuth | 

    try:
        api_response = api_instance.auth_token_create(callback_token_auth)
        print("The response of AuthApi->auth_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_token_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_token_auth** | [**CallbackTokenAuth**](CallbackTokenAuth.md)|  | 

### Return type

[**CallbackTokenAuth**](CallbackTokenAuth.md)

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

# **auth_verify_create**
> CallbackTokenVerification auth_verify_create(callback_token_verification)

This verifies an alias on correct callback token entry using the same logic as auth.
Should be refactored at some point.

### Example

* Api Key Authentication (tokenAuth):

```python
import openapi_client
from openapi_client.models.callback_token_verification import CallbackTokenVerification
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
    api_instance = openapi_client.AuthApi(api_client)
    callback_token_verification = openapi_client.CallbackTokenVerification() # CallbackTokenVerification | 

    try:
        api_response = api_instance.auth_verify_create(callback_token_verification)
        print("The response of AuthApi->auth_verify_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_verify_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **callback_token_verification** | [**CallbackTokenVerification**](CallbackTokenVerification.md)|  | 

### Return type

[**CallbackTokenVerification**](CallbackTokenVerification.md)

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

# **auth_verify_email_create**
> auth_verify_email_create()

This returns a 6-digit callback token we can trade for a user's Auth Token.

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
    api_instance = openapi_client.AuthApi(api_client)

    try:
        api_instance.auth_verify_email_create()
    except Exception as e:
        print("Exception when calling AuthApi->auth_verify_email_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_verify_mobile_create**
> auth_verify_mobile_create()

This returns a 6-digit callback token we can trade for a user's Auth Token.

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
    api_instance = openapi_client.AuthApi(api_client)

    try:
        api_instance.auth_verify_mobile_create()
    except Exception as e:
        print("Exception when calling AuthApi->auth_verify_mobile_create: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

