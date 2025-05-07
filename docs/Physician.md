# Physician


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**gender** | [**PatchedPhysicianGender**](PatchedPhysicianGender.md) |  | [optional] 
**national_code** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**medical_code** | **str** |  | [optional] 
**specialty** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**occupational_clinic** | **int** |  | [optional] 

## Example

```python
from hseagent_sdk.models.physician import Physician

# TODO update the JSON string below
json = "{}"
# create an instance of Physician from a JSON string
physician_instance = Physician.from_json(json)
# print the JSON string representation of the object
print(Physician.to_json())

# convert the object into a dict
physician_dict = physician_instance.to_dict()
# create an instance of Physician from a dict
physician_from_dict = Physician.from_dict(physician_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


