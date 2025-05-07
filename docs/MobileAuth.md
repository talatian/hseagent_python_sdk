# MobileAuth

Abstract class that returns a callback token based on the field given Returns a token if valid, None or a message if not.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mobile** | **str** |  | 

## Example

```python
from hseagent_sdk.models.mobile_auth import MobileAuth

# TODO update the JSON string below
json = "{}"
# create an instance of MobileAuth from a JSON string
mobile_auth_instance = MobileAuth.from_json(json)
# print the JSON string representation of the object
print(MobileAuth.to_json())

# convert the object into a dict
mobile_auth_dict = mobile_auth_instance.to_dict()
# create an instance of MobileAuth from a dict
mobile_auth_from_dict = MobileAuth.from_dict(mobile_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


