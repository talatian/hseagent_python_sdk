# PatchedDepartment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.patched_department import PatchedDepartment

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedDepartment from a JSON string
patched_department_instance = PatchedDepartment.from_json(json)
# print the JSON string representation of the object
print(PatchedDepartment.to_json())

# convert the object into a dict
patched_department_dict = patched_department_instance.to_dict()
# create an instance of PatchedDepartment from a dict
patched_department_from_dict = PatchedDepartment.from_dict(patched_department_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


