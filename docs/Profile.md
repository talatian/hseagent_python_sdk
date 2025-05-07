# Profile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** |  | [readonly] 
**name** | **str** |  | [readonly] 
**organization** | **str** |  | [readonly] 
**mobile** | **str** |  | [readonly] 
**email** | **str** |  | [optional] 
**role** | **str** |  | [readonly] 
**date_joined** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.profile import Profile

# TODO update the JSON string below
json = "{}"
# create an instance of Profile from a JSON string
profile_instance = Profile.from_json(json)
# print the JSON string representation of the object
print(Profile.to_json())

# convert the object into a dict
profile_dict = profile_instance.to_dict()
# create an instance of Profile from a dict
profile_from_dict = Profile.from_dict(profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


