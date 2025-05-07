# PatchedClinicProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from hseagent_sdk.models.patched_clinic_profile import PatchedClinicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedClinicProfile from a JSON string
patched_clinic_profile_instance = PatchedClinicProfile.from_json(json)
# print the JSON string representation of the object
print(PatchedClinicProfile.to_json())

# convert the object into a dict
patched_clinic_profile_dict = patched_clinic_profile_instance.to_dict()
# create an instance of PatchedClinicProfile from a dict
patched_clinic_profile_from_dict = PatchedClinicProfile.from_dict(patched_clinic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


