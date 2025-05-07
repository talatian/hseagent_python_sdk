# CallbackTokenVerification

Takes a user and a token, verifies the token belongs to the user and validates the alias that the token was sent from.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**token** | **str** |  | 

## Example

```python
from hseagent_sdk.models.callback_token_verification import CallbackTokenVerification

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackTokenVerification from a JSON string
callback_token_verification_instance = CallbackTokenVerification.from_json(json)
# print the JSON string representation of the object
print(CallbackTokenVerification.to_json())

# convert the object into a dict
callback_token_verification_dict = callback_token_verification_instance.to_dict()
# create an instance of CallbackTokenVerification from a dict
callback_token_verification_from_dict = CallbackTokenVerification.from_dict(callback_token_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


