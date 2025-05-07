# PatchedHSEProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**national_code** | **str** |  | [optional] 
**organization** | **str** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from hseagent_sdk.models.patched_hse_profile import PatchedHSEProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedHSEProfile from a JSON string
patched_hse_profile_instance = PatchedHSEProfile.from_json(json)
# print the JSON string representation of the object
print(PatchedHSEProfile.to_json())

# convert the object into a dict
patched_hse_profile_dict = patched_hse_profile_instance.to_dict()
# create an instance of PatchedHSEProfile from a dict
patched_hse_profile_from_dict = PatchedHSEProfile.from_dict(patched_hse_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


