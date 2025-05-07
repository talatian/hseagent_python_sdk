# PatchedPhysician


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | [**PatchedPhysicianGender**](PatchedPhysicianGender.md) |  | [optional] 
**national_code** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**medical_code** | **str** |  | [optional] 
**specialty** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**occupational_clinic** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.patched_physician import PatchedPhysician

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPhysician from a JSON string
patched_physician_instance = PatchedPhysician.from_json(json)
# print the JSON string representation of the object
print(PatchedPhysician.to_json())

# convert the object into a dict
patched_physician_dict = patched_physician_instance.to_dict()
# create an instance of PatchedPhysician from a dict
patched_physician_from_dict = PatchedPhysician.from_dict(patched_physician_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


