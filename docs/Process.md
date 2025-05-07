# Process


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**hazards** | [**List[ObservationType]**](ObservationType.md) |  | [readonly] 
**hazard_ids** | **List[int]** |  | 
**organization** | **int** |  | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [readonly] 

## Example

```python
from hseagent_sdk.models.process import Process

# TODO update the JSON string below
json = "{}"
# create an instance of Process from a JSON string
process_instance = Process.from_json(json)
# print the JSON string representation of the object
print(Process.to_json())

# convert the object into a dict
process_dict = process_instance.to_dict()
# create an instance of Process from a dict
process_from_dict = Process.from_dict(process_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


