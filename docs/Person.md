# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**department** | **str** |  | [readonly] 
**role** | **str** |  | [readonly] 
**status** | **str** |  | [readonly] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**father_name** | **str** |  | 
**gender** | [**GenderEnum**](GenderEnum.md) |  | 
**national_code** | **str** |  | 
**insurance_code** | **str** |  | [optional] 
**employee_code** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**education_level** | [**PatchedPersonEducationLevel**](PatchedPersonEducationLevel.md) |  | [optional] 
**marital_status** | [**PatchedPersonMaritalStatus**](PatchedPersonMaritalStatus.md) |  | [optional] 
**number_of_children** | **int** |  | [optional] 
**military_service** | [**PatchedPersonMilitaryService**](PatchedPersonMilitaryService.md) |  | [optional] 
**exemption_reason** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 
**organization** | **int** |  | 

## Example

```python
from openapi_client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


