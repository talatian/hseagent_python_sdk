# CallbackTokenAuth

Abstract class inspired by DRF's own token serializer. Returns a user if valid, None or a message if not.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**token** | **str** |  | 

## Example

```python
from hseagent_sdk.models.callback_token_auth import CallbackTokenAuth

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackTokenAuth from a JSON string
callback_token_auth_instance = CallbackTokenAuth.from_json(json)
# print the JSON string representation of the object
print(CallbackTokenAuth.to_json())

# convert the object into a dict
callback_token_auth_dict = callback_token_auth_instance.to_dict()
# create an instance of CallbackTokenAuth from a dict
callback_token_auth_from_dict = CallbackTokenAuth.from_dict(callback_token_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


