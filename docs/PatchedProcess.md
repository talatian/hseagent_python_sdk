# PatchedProcess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**hazards** | [**List[ObservationType]**](ObservationType.md) |  | [optional] [readonly] 
**hazard_ids** | **List[int]** |  | [optional] 
**organization** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.patched_process import PatchedProcess

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedProcess from a JSON string
patched_process_instance = PatchedProcess.from_json(json)
# print the JSON string representation of the object
print(PatchedProcess.to_json())

# convert the object into a dict
patched_process_dict = patched_process_instance.to_dict()
# create an instance of PatchedProcess from a dict
patched_process_from_dict = PatchedProcess.from_dict(patched_process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


