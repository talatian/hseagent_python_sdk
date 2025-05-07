# PatchedPerson


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**department** | **str** |  | [optional] [readonly] 
**role** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**father_name** | **str** |  | [optional] 
**gender** | [**GenderEnum**](GenderEnum.md) |  | [optional] 
**national_code** | **str** |  | [optional] 
**insurance_code** | **str** |  | [optional] 
**employee_code** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**education_level** | [**PatchedPersonEducationLevel**](PatchedPersonEducationLevel.md) |  | [optional] 
**marital_status** | [**PatchedPersonMaritalStatus**](PatchedPersonMaritalStatus.md) |  | [optional] 
**number_of_children** | **int** |  | [optional] 
**military_service** | [**PatchedPersonMilitaryService**](PatchedPersonMilitaryService.md) |  | [optional] 
**exemption_reason** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | **int** |  | [optional] 

## Example

```python
from hseagent_sdk.models.patched_person import PatchedPerson

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedPerson from a JSON string
patched_person_instance = PatchedPerson.from_json(json)
# print the JSON string representation of the object
print(PatchedPerson.to_json())

# convert the object into a dict
patched_person_dict = patched_person_instance.to_dict()
# create an instance of PatchedPerson from a dict
patched_person_from_dict = PatchedPerson.from_dict(patched_person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


