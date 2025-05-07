# PatchedRole


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
from hseagent_sdk.models.patched_role import PatchedRole

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedRole from a JSON string
patched_role_instance = PatchedRole.from_json(json)
# print the JSON string representation of the object
print(PatchedRole.to_json())

# convert the object into a dict
patched_role_dict = patched_role_instance.to_dict()
# create an instance of PatchedRole from a dict
patched_role_from_dict = PatchedRole.from_dict(patched_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


