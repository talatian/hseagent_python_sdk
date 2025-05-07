# PatchedBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.patched_branch import PatchedBranch

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedBranch from a JSON string
patched_branch_instance = PatchedBranch.from_json(json)
# print the JSON string representation of the object
print(PatchedBranch.to_json())

# convert the object into a dict
patched_branch_dict = patched_branch_instance.to_dict()
# create an instance of PatchedBranch from a dict
patched_branch_from_dict = PatchedBranch.from_dict(patched_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


