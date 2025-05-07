# ClinicProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**phone** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.clinic_profile import ClinicProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ClinicProfile from a JSON string
clinic_profile_instance = ClinicProfile.from_json(json)
# print the JSON string representation of the object
print(ClinicProfile.to_json())

# convert the object into a dict
clinic_profile_dict = clinic_profile_instance.to_dict()
# create an instance of ClinicProfile from a dict
clinic_profile_from_dict = ClinicProfile.from_dict(clinic_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


